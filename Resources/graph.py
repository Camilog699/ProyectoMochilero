from Resources.places import Place
from Resources.edge import Edge


class Graph:
    def __init__(self):
        self.places = []
        self.edges = []

    def Get_Vertex(self, id):
        if self.Exist(id):
            return self.places[id]
        return None

    def Exist(self, id):
        return id in self.places[id]

    def add_place(self, label, name, mintime, jobs, thingtodo):
        newplace = Place(label, name, mintime, jobs, thingtodo)
        if newplace not in self.places:
            self.places.append(newplace)

    def add_edge(self, value, vertexA, vertexB, forms):
        newedge = Edge(value, vertexA, vertexB, forms)
        if newedge not in self.edges:
            self.edges.append(newedge)
            vertexA.goingto.append(vertexB)
