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
def create_graph():
    print("Wybierz rodzaj grafu: ")
    print("1. Skierowany")
    print("2. Nieskierowany")
    print("3. Ważony")
    print("4. Inny możliwy")

    choice = int(input("Wybierz typ grafu (podaj numer opcji): "))
    num_vertices = int(input("Podaj liczbę wierzchołków: "))
    num_edges = int(input("Podaj liczbę połączeń pomiędzy wierzchołkami: "))

    graph = Graph()

    for i in range(num_vertices):
        graph.addVertex(i)

    for _ in range(num_edges):
        source = int(input("Podaj wierzchołek źródłowy: "))
        target = int(input("Podaj wierzchołek docelowy: "))

        if choice == 3:  # Jeśli graf jest ważony, pobierz wagę krawędzi
            weight = float(input("Podaj wagę krawędzi: "))
            graph.addEdge(source, target, weight)
        else:
            graph.addEdge(source, target)

        if choice == 2:  # Jeśli graf jest nieskierowany, zaktualizuj także krawędź w drugim kierunku
            graph.addEdge(target, source)

    return graph


def display_adjacency_list(graph):
    print("\nLista sąsiedztwa:")
    for vertex in graph:
        print(vertex)


def display_graph(graph):
    print("\nInterpretacja graficzna:")
    for vertex in graph:
        print(vertex.getId(), end=": ")
        for neighbor in vertex.getConnections():
            weight = vertex.getWeight(neighbor)
            if weight:
                print(f"{neighbor.getId()}({weight})", end=" ")
            else:
                print(neighbor.getId(), end=" ")
        print()
graph = create_graph()
display_adjacency_list(graph)
display_graph(graph)