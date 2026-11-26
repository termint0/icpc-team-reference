from collections import deque
INF = float("inf")
def spfa(adj, s):
    """Queue-based Bellman-Ford. Returns dist, or None on a negative cycle
    reachable from s."""
    n = len(adj)
    dist = [INF] * n
    cnt = [0] * n
    inq = [False] * n
    dist[s] = 0
    q = deque([s])
    inq[s] = True
    while q:
        u = q.popleft()
        inq[u] = False
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if not inq[v]:
                    cnt[v] += 1
                    if cnt[v] > n:
                        return None
                    inq[v] = True
                    q.append(v)
    return dist
