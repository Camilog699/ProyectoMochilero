from GUI.GUI import GUI
from Json.JSON import JSON
from Resources.algorithms import Algorithms


def main():
    json = JSON()
    graph = json.Read()
    # GUI(graph)
    graph.Dijkstra()

main()
