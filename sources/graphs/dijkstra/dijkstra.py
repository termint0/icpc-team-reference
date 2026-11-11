import heapq
def dijkstra(adj, src):
    """adj[u] = list of (v, w) with w >= 0. Returns (dist, parent).
    dist[v] = inf if unreachable; parent[v] = -1 for src and unreachable."""
    dist = [float('inf')] * len(adj)
    parent = [-1] * len(adj)
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:  # stale entry
            continue
        for v, w in adj[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist, parent
