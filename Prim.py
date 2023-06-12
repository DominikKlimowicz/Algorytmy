class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def prim(graph):
    n = len(graph)
    visited = [False] * n
    parent = [None] * n  # Inicjalizacja listy parent
    queue = Queue()
    queue.enqueue((0, 0))  # Krotka (waga, wierzchołek)
    mst = []

    while not queue.isEmpty():
        w, u = queue.dequeue()
        if visited[u]:
            continue
        visited[u] = True

        for v, weight in graph[u]:
            if not visited[v]:
                queue.enqueue((weight, v))
                parent[v] = u  # Ustawienie poprzednika wierzchołka v

        if u != 0:  # Ignoruj wierzchołek początkowy
            mst.append((u, parent[u], w))

    return mst
