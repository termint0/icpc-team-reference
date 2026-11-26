from collections import deque
from euler_tour import euler_tour
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


def test_tree_tools():
    for _ in range(60):
        n = random.randrange(1, 40)
        adj = rand_tree(n)
        D = tree_dists(adj)
        for _ in range(50):
            u, v = (random.randrange(n), random.randrange(n))
        tin, tout, order = euler_tour(adj, 0)
        assert sorted(order) == list(range(n))
        for u in range(n):
            for v in range(n):
                anc = tin[u] <= tin[v] < tout[u]
                assert anc == (D[0][u] + D[u][v] == D[0][v])
        wadj = [[] for _ in range(n)]
        for u in range(n):
            for v in adj[u]:
                wadj[u].append((v, 1 + (u * 7 + v * 7) % 5))
