from collections import deque
from rerooting import rerooting
import random


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


def rand_tree(n):
    adj = [[] for _ in range(n)]
    for v in range(1, n):
        u = random.randrange(v)
        adj[u].append(v)
        adj[v].append(u)
    return adj


def tree_dists(adj):
    return [bfs(adj, s) for s in range(len(adj))]


def test_rerooting():
    for _ in range(60):
        n = random.randrange(1, 30)
        adj = rand_tree(n)
        D = tree_dists(adj)
        ecc = rerooting(adj, 0, max, lambda x, c, p: x + 1, lambda v, m: m)
        assert ecc == [max(r) for r in D]
        # sum of distances
        add = lambda a, b: (a[0] + b[0], a[1] + b[1])
        res = rerooting(adj, (0, 0), add, lambda x, c, p: (x[0], x[1] + x[0]), lambda v, m: (m[0] + 1, m[1]))
        assert [r[1] for r in res] == [sum(r) for r in D]
        assert all(r[0] == n for r in res)
