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

    def Dijkstra(self, placeA, places, edges, edgesOrigin, state, visitPlaces, minCost, minT):
        temp = []
        visited = []
        minplace = None
        minvalue = inf
        i = 0
        visitPlaces.append(placeA)
        if len(visitPlaces) == len(places):
            return visitPlaces
        for edge in edgesOrigin:
            if edge.vertexA is placeA:
                temp.append(edge)
                edges.append(edge)
        for edge in temp:
            if (edge.vertexA.status[0] + edge.value) < edge.vertexB.status[0]:
                edge.vertexB.status[0] = edge.vertexA.status[0] + edge.value
                edge.vertexB.status[1] = edge.vertexA.label
        for edge in edges:
            if edge.vertexB.status[0] < minvalue and edge.vertexB not in visitPlaces:
                minvalue = edge.vertexB.status[0]
                minplace = edge.vertexB
        visited.append(minplace)
        visitPlaces = self.Dijkstra(
            minplace, places, edges, edgesOrigin, state, visitPlaces)
        return visitPlaces
