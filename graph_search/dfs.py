from collections import deque
from graph_search.vertex import Vertex


class DFS:

    def dfsearchstack(self, root=Vertex(-1)):
        dfstack = deque()
        root.visited = True

        dfstack.append(root)
        while True:
            try:
                currentvertex = dfstack.pop()
                print(currentvertex.vertextostring(), "-> ", end='')
                for v in currentvertex.neighborList:
                    if not v.visited:
                        v.visited = True
                        dfstack.append(v)

            except IndexError:
                print("empty")
                break

    def dfsearchdepth(self, root=Vertex(-1), target=Vertex(-1), maxdepth=0):
        dfstack = deque()
        root.visited = True

        dfstack.append(root)
        while len(dfstack) > 0:
            currentvertex = dfstack.pop()
            print(currentvertex.vertextostring(), "", end='')

            if currentvertex.value == target.value:
                print("target found!")
                return True

            if currentvertex.depth >= maxdepth:
                continue

            for v in currentvertex.neighborList:
                v.depth = currentvertex.depth + 1
                dfstack.append(v)

        return False



    def dfsearchrec(self, root=Vertex(-1)):
        print(root.vertextostring(), "-> ", end='')
        root.visited = True
        for v in root.neighborList:
            if not v.visited:
                self.dfsearchrec(v)
