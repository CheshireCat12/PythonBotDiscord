import json

class StuffleQuest:
	filename = "nodeList.json"
	def __init__(self):
		self.dataGame = get_data_from_json(self.filename)
		self.currentNode = "nodeRoot"

	@property
	def currentNode(self):
		return self._currentNode

	@property
	def dataGame(self):
		return self._dataGame

	@currentNode.setter
	def currentNode(self, currentNode):
		self._currentNode = self.dataGame[currentNode]

	@dataGame.setter
	def dataGame(self, dataGame):
		self._dataGame = dataGame

def get_data_from_json(filename):
	with open(filename) as data_file:
		data = json.load(data_file)
	return data

if __name__ == "__main__":
	print("toto")
	game = StuffleQuest()
	print(game.dataGame)
	print(game.currentNode)
