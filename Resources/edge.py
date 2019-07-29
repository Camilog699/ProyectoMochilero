from pygame import Rect


class Edge:
    def __init__(self, value, vertexA, vertexB, forms):
        self.value = value
        self.vertexA = vertexA
        self.vertexB = vertexB
        self.forms = forms
        self.isbi = False
        self.obs = False
<<<<<<< HEAD
        self.line = None
        self.rect = (vertexA.rect.x, vertexA.rect.y, 20, 20)
=======
        self.linea = None
        self.rect = Rect(vertexA.rect.x, vertexA.rect.y, 20, 20)
>>>>>>> 0f06b91b9e968cc86d9a25fd160a5d1dfee20e74
        self.color = (0, 0, 0)

    def __eq__(self, edge):
        return (self.value == edge.value and self.vertexA == edge.vertexA and
                self.vertexB == edge.vertexB and self.forms == edge.forms)

    def __lt__(self, edge):
        return self.value < edge.value
