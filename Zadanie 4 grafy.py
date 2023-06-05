import math
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}  # lista sąsiedztwa z wagami

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        return self.vertList.get(n)

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

def dijkstra(graph, start):
    distances = {vertex: math.inf for vertex in graph.getVertices()}  # słownik przechowujący koszty dotarcia do wierzchołków
    previous = {}  # słownik przechowujący poprzednie wierzchołki w najkrótszej drodze
    unvisited = set(graph.getVertices())  # zbiór nieodwiedzonych wierzchołków

    distances[start.getId()] = 0

    while unvisited:
        current_vertex = None
        min_distance = math.inf

        for vertex in unvisited:
            if distances[vertex] < min_distance:
                current_vertex = vertex
                min_distance = distances[vertex]

        if min_distance == math.inf:
            break

        unvisited.remove(current_vertex)

        for neighbor in graph.getVertex(current_vertex).getConnections():
            weight = graph.getVertex(current_vertex).getWeight(neighbor)
            distance = distances[current_vertex] + weight

            if distance < distances[neighbor.getId()]:
                distances[neighbor.getId()] = distance
                previous[neighbor.getId()] = current_vertex

    return distances, previous


def shortest_path(graph, start, end):
    distances, previous = dijkstra(graph, start)

    if distances[end.getId()] == math.inf:
        return None, None

    path = []
    current_vertex = end.getId()

    while current_vertex:
        path.append(current_vertex)
        current_vertex = previous[current_vertex]

    path.reverse()
    return path, distances[end.getId()]


# Użycie programu
# Tworzenie grafu
graph = Graph()
vertexA = graph.addVertex('A')
vertexB = graph.addVertex('B')
vertexC = graph.addVertex('C')
vertexD = graph.addVertex('D')
vertexE = graph.addVertex('E')

graph.addEdge(vertexA, vertexB, 5)
graph.addEdge(vertexA, vertexC, 2)
graph.addEdge(vertexB, vertexC, 1)
graph.addEdge(vertexB, vertexD, 3)
graph.addEdge(vertexC, vertexD, 2)
graph.addEdge(vertexD, vertexE, 4)

start_vertex = vertexA
end_vertex = vertexE

path, distance = shortest_path(graph, start_vertex, end_vertex)

if path is None:
    print(f"Nie istnieje ścieżka między wierzchołkami {start_vertex.getId()} a {end_vertex.getId()}")
else:
    print(f"Najkrótsza droga z wierzchołka {start_vertex.getId()} do wierzchołka {end_vertex.getId()}:")
    print(" -> ".join(path))
    print(f"Koszt: {distance}")
