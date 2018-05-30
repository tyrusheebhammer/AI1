from queue import Queue

class BFS:

    def bfs(self, root=Vertex.Vertex(-1)):
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
