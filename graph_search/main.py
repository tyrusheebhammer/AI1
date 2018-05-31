
from graph_search import bfs
from graph_search import vertex
from random import randint


def main():

    vertices = []

    for i in range(6):
        vert = vertex.Vertex(i)
        vertices.append(vertex.Vertex(i))

    for v in vertices:
        rand = randint(0, 5)
        if vertices[rand] not in v.neighborList:
            v.addneighbor(vertices[rand])

    (vertices[0])


if __name__ == '__main__':
    main()
