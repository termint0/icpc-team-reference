INF = float("inf")
def bellman_ford(n, edges, s):
    """Returns dist; -INF for nodes reachable via a negative cycle, INF if
    unreachable."""
    dist = [INF] * n
    dist[s] = 0
    for _ in range(n - 1):
        ch = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                ch = True
        if not ch: break
    for _ in range(n):
        ch = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF
                ch = True
            elif dist[u] == -INF and dist[v] != -INF:
                dist[v] = -INF
                ch = True
        if not ch: break
    return dist
