def kruskal(n, edges):                  # edges: list of (w, u, v)
    dsu = DSU(n)
    total, mst = 0, []
    for w, u, v in sorted(edges):       # cheapest first
        if dsu.union(u, v):             # skip edges that would close a cycle
            total += w
            mst.append((u, v, w))
            if len(mst) == n - 1: break
    return total, mst                   # a forest if the graph is disconnected
