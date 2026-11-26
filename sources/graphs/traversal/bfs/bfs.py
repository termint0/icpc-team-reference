from collections import deque
INF = float("inf")
def bfs(adj, s):
    """Distances (in edges) from s; INF if unreachable."""
    dist = [INF] * len(adj)
    dist[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == INF:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist
