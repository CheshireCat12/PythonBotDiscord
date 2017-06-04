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


if __name__ == "__main__":
    print("toto")
    game = StuffleQuest()
    print(game.dataGame)
    print(game.currentNode["question"])
    game.setCurrentNode("node1")
    lKey = [key for key, value in game.dataGame.items() if value == game.currentNode][0]
    print(lKey)
    #game.currentNode = game.dataGame["node1"]
    print(game.currentNode)
