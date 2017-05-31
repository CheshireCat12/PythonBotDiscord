import json

class StuffleQuest:
	filename = "nodeList.json"
	def __init__(self):
		self.dataGame = get_data_from_json(self.filename)
		self.currentNode = self.dataGame["nodeMenu"]

	def currentNode(self):
		return self.currentNode

	def dataGame(self):
		return self.dataGame

	def currentNode(self, currentNode):
		self.currentNode = self.dataGame[currentNode]

	def dataGame(self, dataGame):
		self.dataGame = dataGame

def get_data_from_json(filename):
	with open(filename, encoding="utf-8") as data_file:
		data = json.load(data_file)
	return data

if __name__ == "__main__":
	print("toto")
	game = StuffleQuest()
	print(game.dataGame)
	print(game.currentNode["question"])
	game.currentNode = game.dataGame["node1"]
	print(game.currentNode)
