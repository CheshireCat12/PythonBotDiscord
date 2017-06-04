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

    def setCurrentNode(self, currentNode):
        self.currentNode = self.dataGame[currentNode]


def get_data_from_json(filename):
    with open(filename, encoding="utf-8") as data_file:
        data = json.load(data_file)
    return data
