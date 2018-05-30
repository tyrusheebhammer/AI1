

from random import randint


def main():
    bfs = BFS()
    ver1 = Vertex(1)
    ver2 = Vertex(value=2)
    ver3 = Vertex(value=3)
    ver4 = BFS.Vertex.Vertex(value=4)
    ver5 = BFS.Vertex.Vertex(value=5)

    vertices = []

    for i in range(6):
        vertices.append(v(i))

    for v in vertices:
        rand = randint(0, 5)
        if vertices[rand] not in v.neighborList:
            v.addneighbor(vertices[rand])

    bfs.bfs(vertices[0])


if __name__ == '__main__':
    main()
