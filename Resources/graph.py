from Resources.places import Place
from Resources.edge import Edge
from Resources.algorithms import Algorithms
from Resources.backpacker import Backpacker


class Graph:
    def __init__(self):
        self.places = []
        self.edges = []
        self.visited = []

    def Get_Vertex(self, id):
        for place in self.places:
            if place.label is id:
                return place

    def Get_Places(self, origin, destiny):
        for edge in self.edges:
            if edge.vertexA is origin and edge.vertexB is destiny:
                return edge

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

    def Dijkstra(self, vertex, cost, time, variable):
        self.visited.clear()
        vertex = vertex
        vertex.status[0] = 0
        vertex.status[1] = vertex.label
        vertex.statusT[0] = 0
        vertex.statusT[1] = vertex.label
        vertex.statusD[0] = 0
        vertex.statusD[1] = vertex.label
        self.visited = Algorithms().Dijkstra(
            vertex, self.places, [], self.edges, True, self.visited, cost, time)
        way = []
        wayF = []
        cont = True
        aux = None

        men = self.visited[0]
        if cost:
            for node in self.visited:
                if node.status[0] > men.status[0] and node.status[0] < variable:
                    men = node

            while cont:
                way.append(men)
                if self.Get_Vertex(men.status[1]) is not men:
                    men = self.Get_Vertex(men.status[1])
                else:
                    cont = False

        elif time:
            for node in self.visited:
                if node.statusT[0] > men.statusT[0] and node.statusT[0] < variable:
                    men = node

            while cont:
                way.append(men)
                if self.Get_Vertex(men.statusT[1]) is not men:
                    men = self.Get_Vertex(men.statusT[1])
                else:
                    cont = False
        else:
            for node in self.visited:
                if node is self.Get_Vertex(variable):
                    men = node

            while cont:
                way.append(men)
                if self.Get_Vertex(men.statusD[1]) is not men:
                    men = self.Get_Vertex(men.statusD[1])
                else:
                    cont = False
        # for i in range(len(way) - 1, -1, -1):
          #  wayF.append(way[i])

        return way

    def evaluate(self, valueIni, timeIni, vertexA, vertexB, transport, things, job):
        newBack = Backpacker(valueIni, timeIni)
        money = False

        for edge in self.edges:
            if edge.forms == "1":
                valueBytrasnport = 8 * edge.value
                timeBytransport = 1 * edge.value
            elif edge.forms == "2":
                valueBytrasnport = 5 * edge.value
                timeBytransport = 5 * edge.value
            elif edge.forms == "3":
                valueBytrasnport = 3 * edge.value
                timeBytransport = 15 * edge.value
            newBack.money = newBack.money - valueBytrasnport
            newBack.time = newBack.time - timeBytransport

        for place in self.places:
            for thing in place.things:
                if thing.type == "mandatory":
                    newBack.time = newBack.time - thing.time
                    newBack.money = newBack.money - thing.cost
                if thing.type == "optional":
                    newBack.time = newBack.time - thing.time
                    newBack.money = newBack.money - thing.cost

            if newBack.work():
                money = self.evaluateMoney(newBack)
                if money:
                    for job in place.jobs:
                        newBack.time = newBack.time - job.time
                        newBack.money = newBack.money + job.gain

    def evaluateMoney(self, backaper):
        if backaper.money < backaper.min:
            return True
        else:
            return False
