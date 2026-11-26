import heapq
def prim(adj):
    """adj[u] = [(v, w)], undirected. Returns (total weight of the spanning
    forest, parent list); parent[root] = -1."""
    n = len(adj)
    seen, parent, total = [False] * n, [-1] * n, 0
    for r in range(n):
        if seen[r]: continue
        pq = [(0, r, -1)]
        while pq:
            w, u, p = heapq.heappop(pq)
            if seen[u]: continue
            seen[u] = True
            parent[u] = p
            total += w
            for v, ww in adj[u]:
                if not seen[v]:
                    heapq.heappush(pq, (ww, v, u))
    return total, parent
