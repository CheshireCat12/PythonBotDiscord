# -*- coding: utf-8 -*-
import asyncio
import json
import zlib
import os
import aiohttp

import interfaceBotStuffle as ibs

TOKEN = os.environ['TOKEN']
URL = "https://discordapp.com/api"
HEADERS = {
    "Authorization": f"Bot {TOKEN}",
    "User-Agent": "DiscordBot (http://he-arc.ch/, 0.1)"
}

async def api_call(path, method="GET", **kwargs):
    """Return the JSON body of a call to Discord REST API."""
    defaults = {"headers": HEADERS}
    kwargs = dict(defaults, **kwargs)
    with aiohttp.ClientSession() as session:
        async with session.request(method, f"{URL}{path}", **kwargs) as response:
            if 200 == response.status:
                return await response.json()
            elif 204 == response.status:
                return {}
            else:
                body = await response.text()
                raise AssertionError(f"{response.status} {response.reason} was unexpected.\n{body}")


async def identify(ws):
    """Task who identify the bot to the web socket (required)"""
    await ws.send_json({'op': 2,
                        'd': {'token': TOKEN,
                              'properties': {},
                              'compress': True,
                              'large_threshold': 250}})


async def start(ws):
    global last_sequence
    with aiohttp.ClientSession() as session:
        async with session.ws_connect(f"{ws}?v=5&encoding=json") as ws:
            async for msg in ws:
                if msg.tp == aiohttp.WSMsgType.TEXT:
                    data = json.loads(msg.data)
                elif msg.tp == aiohttp.WSMsgType.BINARY:
                    data = json.loads(zlib.decompress(msg.data))
                else:
                    print("? toto", msg.tp)
                if data["op"] == 10:  # Hell0
                    asyncio.ensure_future(heartbeat(ws, data['d']['heartbeat_interval']))
                    await identify(ws)
                elif data['op'] == 11:
                    print("< heartbeat ACK")
                elif data['op'] == 0:
                    last_sequence = data['s']
                    if data['t'] == "MESSAGE_CREATE":
                        if data['d']['author']['username'] in ("kimJongUn", "Schnaebele"):
                            answerUser = data["d"]["content"].split(":")
                            game = ibs.interface(answerUser[0], data['d']['author']['username'], data["d"]["content"])
                            task = asyncio.ensure_future(send_message(data['d']['author']['id'],
                                                                      "answer",
                                                                      {"title": ":moyai: Stuffle Quest :moneybag:",
                                                                       "description": game}))
                            if data['d']['content'] == "quit":
                                print("bye bye")
                                await asyncio.wait([task])
                                break
                        else:
                            pass

last_sequence = None


async def heartbeat(ws, interval):
    """Send every interval ms the heartbeat message."""
    while True:
        await asyncio.sleep(interval/1000)
        await ws.send_json({
            "op": 1,
            "d": last_sequence
        })


async def send_message(recipient_id, content, embed=""):
    """Send a message with contenet to the recipient_id"""
    channel = await api_call("/users/@me/channels",
                             "POST",
                             json={"recipient_id": recipient_id})
    if(channel['is_private']):
        return await api_call(f"/channels/{channel['id']}/messages",
                              "POST",
                              json={"content": "", "embed": embed})


async def main():
    """Main program."""
    response = await api_call("/gateway")
    await start(response["url"])


loop = asyncio.get_event_loop()
loop.set_debug(True)
loop.run_until_complete(main())
loop.close()
