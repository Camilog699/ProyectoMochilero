class Edge:
    def __init__(self, value, vertexA, vertexB, forms):
        self.value = value
        self.vertexA = vertexA
        self.vertexB = vertexB
        self.forms = forms
        self.isbi = False

    def __eq__(self, edge):
        return (self.value == edge.value and self.vertexA == edge.vertexA and
                self.vertexB == edge.vertexB and self.forms == edge.forms)
