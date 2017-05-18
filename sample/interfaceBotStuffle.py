import stuffleQuest
import pdb
import os

def interface(action , user, msg, node = "nodeRoot"):
	action = action.lower()
	if action in actionArray:
		game = getGame(user)
		actionArray[action](user = user)
		#game.currentNode = node
		return createResponse(user ,game)
	else:
		return "sorry bad answer"

def getGame(user):
	if not(user in tabPlayer):
		tabPlayer.setdefault(user, stuffleQuest.StuffleQuest())
	game = tabPlayer[user]
	return game

def createResponse(user ,game):
	return game.currentNode["question"].format(user) + "\n :ok_hand: " + game.currentNode["answer"]

def startGame(**kwargs):
	pass

def answerGame(**kwargs):
	user = kwargs["user"]
	tabPlayer[user].currentNode = tabPlayer[user].currentNode["nodeNextLive"]


def saveGame():
	pass

actionArray = {"start" : startGame, "save" : saveGame, "answer" : answerGame}

tabPlayer = {}

def main():
	print(os.environ)
	temp = interface("start", "anthony", "start")
	print(temp)
	temp = interface("toto","anthony","answer","node1")
	print(temp)
	pass

if __name__ == "__main__":
	main()
