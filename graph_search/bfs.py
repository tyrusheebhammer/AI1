from queue import Queue
from graph_search import vertex
class BFS:

    def bfsearch(self, root=vertex.Vertex(-1)):
        bfsqueue = Queue()
        root.visited = True

        bfsqueue.put(root)
        while not bfsqueue.empty():
            currentvertex = bfsqueue.get()
            print(currentvertex.vertextostring + " ")

            for v in currentvertex.neighborList:
                if not v.visited:
                    v.visited = True
                    bfsqueue.put(v)
