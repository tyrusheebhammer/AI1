from graph_search.dfs import DFS
from graph_search.vertex import Vertex


class IDDFS:
    def __init__(self, targetvertex=Vertex(-1)):
        self.targetvertex = targetvertex
        self.isfound = False

    def iddfs(self, root=Vertex(-1)):
        depth = 0
        dfs = DFS()
        while not self.isfound:
            print()
            self.isfound = dfs.dfsearchdepth(root, self.targetvertex, depth)
            depth += 1
