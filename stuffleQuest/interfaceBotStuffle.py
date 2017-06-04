import stuffleQuest
import json


def interface(action, user, msg):
    action = action.lower().strip()
    if action in actionArray:
        try:
            actionArray[action](user=user, msg=msg)
            game = getGame(user)
            return createResponse(user, game)
        except KeyError as e:
            return "Veuillez commencer le jeu avec 'Commencer' SVP."
    else:
        gameState = stuffleQuest.StuffleQuest()
        if action == "aide":
            gameState.setCurrentNode("nodeHelp")
        return createResponse(user, gameState)


def getGame(user):
    game = tabPlayer[user]
    return game


def createResponse(user, game):
    return game.currentNode["question"].format(user)


def startGame(user):
    tabPlayer.setdefault(user, stuffleQuest.StuffleQuest())
    return tabPlayer(user)


def answerGame(**kwargs):
    user = kwargs["user"]
    msg = kwargs["msg"]
    game = tabPlayer[user]
    if tabPlayer[user].currentNode["answer"] in msg.lower():
        game.setCurrentNode(game.currentNode["nodeNextLive"])
    else:
        game.setCurrentNode(game.currentNode["nodeNextDead"])


def saveGame(**kwargs):
    user = kwargs["user"]
    with open("save.json", 'r') as f:
        temp = json.load(f)
    temp[user] = [key for key, value in tabPlayer[user].dataGame.items() if value == tabPlayer[user].currentNode][0]
    with open('save.json', 'w', encoding='utf8') as f:
        json.dump(temp, f, ensure_ascii=False)


def newGame(**kwargs):
    user = kwargs["user"]
    tabPlayer.setdefault(user, stuffleQuest.StuffleQuest())
    tabPlayer[user].setCurrentNode("node1")


def continueGame(**kwargs):
    user = kwargs['user']
    with open("save.json", 'r') as f:
        temp = json.load(f)
    newGame(user=user)
    try:
        tabPlayer[user].setCurrentNode(temp[user])
    except KeyError as e:
        print("Creation d'une nouvelle parties")


actionArray = {
    "sauvegarder": saveGame,
    "répondre": answerGame,
    "commencer": newGame,
    "continuer": continueGame
}

tabPlayer = {}
