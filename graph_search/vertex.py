


class Vertex:
    def __init__(self, value=0):
        self.value = value
        self.visited = False
        self.neighborList = []

    def vertextostring(self):
        return str(self.value)

    def addneighbor(self, neighbor):
        self.neighborList.append(neighbor)
