class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def engueue(self, item):
        self.items.insert(0, item)

    def denqueue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def BFS(graph, start):
    n=len(graph)
    visited=[False] * n
    d = [-1] * n
    p = [-1] * n

    visited[start] = True
    d[start] = 0
    Q=Queue()
    Q.engueue(start)

    while not Q.isEmpty():
        u = Q.denqueue()

        for v in range(n):
            if graph [u][v] == 1 and not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                p[v] = u
                Q.engueue(v)

    return visited, d, p



graph = [
    [0, 1, 0, 1, 0, 0],
[0, 1, 0, 1, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 1, 1],
[0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 1],
]

start_V=3
visited, distance, parent = (BFS(graph, start_V))
for v in range(len(graph)):
    print(f"Wierzchołek {v}: visited = {visited[v]},\n distance = {distance[v]},\n parent = {parent}")