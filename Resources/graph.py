from Resources.places import Place
from Resources.edge import Edge
from Resources.algorithms import Algorithms


class Graph:
    def __init__(self):
        self.places = []
        self.edges = []
        self.visited = []

    def Get_Vertex(self, id):
        for place in self.places:
            if place.label is id:
                return place

    def add_place(self, label, name, mintime, jobs, thingtodo):
        newplace = Place(label, name, mintime, jobs, thingtodo)
        pas = True
        for place in self.places:
            if newplace == place:
                pas = False

        if pas:
            self.places.append(newplace)

    def add_edge(self, value, vertexA, vertexB, forms):
        newedge = Edge(value, vertexA, vertexB, forms)
        newedgeB = Edge(value, vertexA, vertexB, forms)
        pas = True
        pas1 = False
        for edge in self.edges:
            if newedge == edge:
                pas = False
            if newedgeB == edge:
                pas1 = True
                edge.isbi = True

        if pas1:
            vertexA.goings.append(vertexB)
        if pas and not pas1:
            self.edges.append(newedge)
            vertexA.goings.append(vertexB)

    def min_whit_money(self):
        pass

    def BFS(self):
        self.visited.clear()
        self.visited = Algorithms().BFS(self.visited, [self.places[0]])

    def DFS(self):
        self.visited.clear()
        self.visited = Algorithms().DFS(self.visited, self.places[0])

    def Dijkstra(self):
        self.visited.clear()
        vertex = self.Get_Vertex('A')
        vertex.status[0] = 0
        vertex.status[1] = vertex.label
        self.visited = Algorithms().Dijkstra(
            vertex, self.places, [], self.edges, True, self.visited)
        show = []
        for edge in self.edges:
            if edge.vertexA not in show:
                print(f"{edge.vertexA.label} = {edge.vertexA.status}")
                show.append(edge.vertexA)
            if edge.vertexB not in show:
                print(f"{edge.vertexB.label} = {edge.vertexB.status}")
                show.append(edge.vertexB)
