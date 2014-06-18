# Depth First Traversal

# Graph Definition
class Neighbor:
    def __init__(self, id, next = None):
        self.id = id
        self.next = next

class Vertex:
    def __init__(self, value, neighbor = None):
        self.value = value
        self.neighbors = neighbor

class Graph:
    def __init__(self):
        self.adjLists = []

    def addVertex(self, vertex):
        self.adjLists.append(vertex)

    def vertexCount(self):
        return len(self.adjLists)

    def dfs(self):
        marked = [False] * self.vertexCount()
        for index in range(0, len(self.adjLists)):
            if not marked[index]:
                self.__dfs(index, marked)

    def __dfs(self, vertexId, marked):
        marked[vertexId] = True
        print("%s " %self.adjLists[vertexId].value, end ="")

        current = self.adjLists[vertexId].neighbors
        while current:
            if not marked[current.id]:
                self.__dfs(current.id, marked)
            current = current.next

# Graph
v0 = Vertex("A", Neighbor(1, Neighbor(2)))
v1 = Vertex("B", Neighbor(4))
v2 = Vertex("C", Neighbor(3, Neighbor(4)))
v3 = Vertex("D", Neighbor(0))
v4 = Vertex("E")

# A (B.C)
# B (E)
# C (D,E)
# D (A)

g = Graph()
g.addVertex(v0)
g.addVertex(v1)
g.addVertex(v2)
g.addVertex(v3)
g.addVertex(v4)
g.dfs()