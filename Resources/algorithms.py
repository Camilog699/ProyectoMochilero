from math import inf
from Resources.places import Place


class Algorithms:

    def BFS(self, visited, trail):
        if len(trail) == 0:
            return visited
        for place in trail[0].adjacencies:
            if place.label not in visited and place not in trail:
                trail.append(place)
        visited.append(trail[0].label)
        trail.remove(trail[0])
        return self.BFS(visited, trail)

    def DFS(self, visited, place):
        if place.label in visited:
            return visited

        visited.append(place.label)
        for adjacency in place.adjacencies:
            visited = self.DFS(visited, adjacency)
        return visited

    def Dijkstra(self, placeA, places, edges, edgesOrigin, state, visitPlaces, minCost, minTime):
        temp = []
        visited = []
        minplace = None
        minvalue = inf
        i = 0
        cost = 0
        visitPlaces.append(placeA)
        if len(visitPlaces) == len(places):
            return visitPlaces
        for edge in edgesOrigin:
            if edge.vertexA is placeA:
                temp.append(edge)
                edges.append(edge)
        for edge in temp:
            if minCost:
                if (edge.vertexA.status[0] + edge.value) < edge.vertexB.status[0]:
                    for thing in edge.vertexB.things:
                        if thing.type == 'mandatory':
                            cost += thing.cost
                    edge.vertexB.status[0] = edge.vertexA.status[0] + \
                        edge.value + cost
                    edge.vertexB.status[1] = edge.vertexA.label
            elif minTime:
                if (edge.vertexA.statusT[0] + edge.value) < edge.vertexB.statusT[0]:
                    for thing in edge.vertexB.things:
                        if thing.type == 'mandatory':
                            cost += thing.time + edge.vertexB.minTimeHere
                    edge.vertexB.statusT[0] = edge.vertexA.statusT[0] + \
                        edge.value + cost
                    edge.vertexB.statusT[1] = edge.vertexA.label
            else:
                if (edge.vertexA.statusD[0] + edge.value) < edge.vertexB.statusD[0]:
                    edge.vertexB.statusD[0] = edge.vertexA.statusD[0] + edge.value
                    edge.vertexB.statusD[1] = edge.vertexA.label
        for edge in edges:
            if minCost:
                if edge.vertexB.status[0] < minvalue and edge.vertexB not in visitPlaces:
                    minvalue = edge.vertexB.status[0]
                    minplace = edge.vertexB
            elif minTime:
                if edge.vertexB.statusT[0] < minvalue and edge.vertexB not in visitPlaces:
                    minvalue = edge.vertexB.statusT[0]
                    minplace = edge.vertexB
            else:
                if edge.vertexB.statusD[0] < minvalue and edge.vertexB not in visitPlaces:
                    minvalue = edge.vertexB.statusD[0]
                    minplace = edge.vertexB
        visited.append(minplace)
        visitPlaces = self.Dijkstra(
            minplace, places, edges, edgesOrigin, state, visitPlaces, minCost, minTime)
        return visitPlaces
