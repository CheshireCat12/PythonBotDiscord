import stuffleQuest
#import pdb
import os
import Command

def interface(action , user, msg, node = "nodeMenu"):
	action = action.lower().strip()
	if action in actionArray:
		try:
			actionArray[action](user = user, msg = msg)
			game = getGame(user)
			return createResponse(user, game)
		except KeyError as e:
			return "Veuillez instancier le jeu avec 'Nouveau jeu' SVP."
	else:
		gameState = stuffleQuest.StuffleQuest()
		if action == "aide":
			gameState.currentNode = gameState.dataGame["nodeHelp"]

		return createResponse(user, gameState)

def getGame(user):
	game = tabPlayer[user]
	return game

def createResponse(user ,game):
	return game.currentNode["question"].format(user)

def startGame(user):
	tabPlayer.setdefault(user, stuffleQuest.StuffleQuest())
	return tabPlayer(user)

def answerGame(**kwargs):
	user = kwargs["user"]
	msg = kwargs["msg"]
	print("je passe par la")
	if tabPlayer[user].currentNode["answer"] in msg.lower():
		tabPlayer[user].currentNode = tabPlayer[user].dataGame[tabPlayer[user].currentNode["nodeNextLive"]]
	else:
		tabPlayer[user].currentNode = tabPlayer[user].dataGame[tabPlayer[user].currentNode["nodeNextDead"]]
	print(tabPlayer[user].currentNode)

def saveGame():
	pass


def newGame(**kwargs):
	user = kwargs["user"]
	tabPlayer.setdefault(user, stuffleQuest.StuffleQuest())
	tabPlayer[user].currentNode = tabPlayer[user].dataGame["node1"]

def continueGame():
	print("continue le game")
	pass


actionArray = {"sauvegarder" : saveGame, "répondre" : answerGame, "commencer" : newGame, "continuer" : continueGame}

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
