from collections import deque
INF = float("inf")
def zero_one_bfs(adj, s):
    """adj[u] = [(v, w)] with w in {0, 1}."""
    dist = [INF] * len(adj)
    dist[s] = 0
    dq = deque([s])
    while dq:
        u = dq.popleft()
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if w == 0: dq.appendleft(v)
                else: dq.append(v)
    return dist
