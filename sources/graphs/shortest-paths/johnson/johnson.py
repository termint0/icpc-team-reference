import heapq
INF = float("inf")
def johnson(n, edges):
    """All-pairs shortest paths with negative edges. Returns matrix or None
    if a negative cycle exists."""
    h = [0] * n
    for _ in range(n):
        ch = False
        for u, v, w in edges:
            if h[u] + w < h[v]:
                h[v] = h[u] + w
                ch = True
        if not ch: break
    else: return None
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w + h[u] - h[v]))
    res = []
    for s in range(n):
        dist = [INF] * n
        dist[s] = 0
        pq = [(0, s)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]: continue
            for v, w in adj[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))
        res.append([dist[v] - h[s] + h[v] if dist[v] != INF else INF for v in range(n)])
    return res
