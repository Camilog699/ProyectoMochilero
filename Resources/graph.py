from Resources.places import Place
from Resources.edge import Edge


class Graph:
    def __init__(self):
        self.places = []
        self.edges = []

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
