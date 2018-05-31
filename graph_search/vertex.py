


class Vertex:
    def __init__(self, value=0):
        self.value = value
        self.visited = False
        self.neighborList = []
        self.depth = 0

    def vertextostring(self):
        return str(self.value)

    def addneighbor(self, neighbor):
        self.neighborList.append(neighbor)
