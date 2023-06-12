def kruskal(graph):
    def find(parent, i):
        if parent[i] == i:
            return i
        return find(parent, parent[i])

    def union(parent, rank, x, y):
        x_root = find(parent, x)
        y_root = find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    edges = []
    num_vertices = len(graph)
    for u in range(num_vertices):
        for v, w in graph[u]:
            edges.append((w, u, v))
    edges.sort()

    mst = []
    parent = [i for i in range(num_vertices)]
    rank = [0] * num_vertices

    for w, u, v in edges:
        if find(parent, u) != find(parent, v):
            mst.append((u, v, w))
            union(parent, rank, u, v)

    return mst


