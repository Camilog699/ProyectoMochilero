from GUI.GUI import GUI
from Json.JSON import JSON


def main():
    json = JSON()
    graph = json.Read()
    GUI(graph)

main()
