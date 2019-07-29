from GUI.GUI import GUI
from Json.JSON import JSON
from Resources.algorithms import Algorithms
from math import inf


def main():
    json = JSON()
    graph = json.Read()
    GUI(graph)


main()
