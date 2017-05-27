import stuffleQuest
#import pdb
import os
import Command

def interface(action , user, msg, node = "nodeRoot"):
	action = action.lower()
	if action in actionArray:
		game = getGame(user)
		actionArray[action](user = user, msg = msg)
		#game.currentNode = node
		return createResponse(user ,game)
	else:
		return "Sorry bad action"

def actionInGame(action):
	if action == "\u25b6":
		print("toto en vacance")
	elif action == "\u23ef":
		pass
	elif action == "\U0001f198":
		print("j'ai besion d'aiiiiide")

def getGame(user):
	if not(user in tabPlayer):
		tabPlayer.setdefault(user, stuffleQuest.StuffleQuest())
	game = tabPlayer[user]
	return game

def createResponse(user ,game):
	return game.currentNode["question"].format(user)

def startGame(**kwargs):
	pass

def answerGame(**kwargs):
	user = kwargs["user"]
	msg = kwargs["msg"]
	if tabPlayer[user].currentNode["answer"] in msg.lower():
		tabPlayer[user].currentNode = tabPlayer[user].currentNode["nodeNextLive"]
	else:
		tabPlayer[user].currentNode = tabPlayer[user].currentNode["nodeNextDead"]


def saveGame():
	pass


def newGame():
	pass

def continueGame():
	print("continue le game")
	pass

actionArray = {"commencer" : startGame, "sauvegarder" : saveGame, "répondre" : answerGame, "nouveau jeu" : newGame, "continuer" : continueGame}

tabPlayer = {}

#commande = Command.Command()

def main():
	#commande = Command.Command()
	#commade.do("continueGame")
	pass

if __name__ == "__main__":
	main()

	if  "c'est toto la réponse" in "toto":
		print("marchre")
	else:
		print("marche pas")
