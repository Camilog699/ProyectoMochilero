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

    def Dijkstra(self, placeA, edges, state):
        if not state:
            return edges
        temp = []
        minplace = Place('', '', 0, [], [])
        minvalue = inf
        change = False
        for edge in edges:
            if edge.vertexA is placeA or edge.vertexB is placeA:
                temp.append(edge)
        for edge in temp:
            if placeA is edge.vertexA:
                if (edge.vertexA.status[0] + edge.value) < edge.vertexB.status[0]:
                    edge.vertexB.status[0] = edge.vertexA.status[0] + edge.value
                    edge.vertexB.status[1] = edge.vertexA
                    state = True
                else:
                    state = False
            else:
                if (edge.vertexB.status[0] + edge.value) < edge.vertexA.status[0]:
                    edge.vertexA.status[0] = edge.vertexB.status[0] + edge.value
                    edge.vertexA.status[1] = edge.vertexA
                    state = True
                else:
                    state = False
        for place in placeA.goings:
            if place.status[0] < minvalue:
                minvalue = place.status[0]
                minplace = place
        edges = self.Dijkstra(minplace, edges, state)
        return edges
