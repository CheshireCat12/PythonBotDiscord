import json
from anytree import Node, RenderTree

data = []
with open('nodeList.json') as data_file:
    data = json.load(data_file)

print(data)

print(data["nodeRoot"])
