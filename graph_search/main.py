from graph_search.bfs import BFS
from graph_search.vertex import Vertex
from graph_search.dfs import DFS
from random import randint


def main():
    vertices = []

    for i in range(5):
        vertices.append(Vertex(i))

    for v in vertices:
        for _ in range(4):
            rand = randint(0, 4)
            if vertices[rand] not in v.neighborList:
                v.addneighbor(vertices[rand])
                print("added", vertices[rand].vertextostring(), "to", v.vertextostring(), "neighbor list")

    bfs = BFS()
    dfs = DFS()
    algos = [bfs.bfsearch, dfs.dfsearchstack, dfs.dfsearchrec]
    for v in vertices:
        print(v.vertextostring(), "--------------------")
        for s in algos:
            s(v)
            for x in vertices:
                x.visited = False
            print()


if __name__ == '__main__':
    main()
