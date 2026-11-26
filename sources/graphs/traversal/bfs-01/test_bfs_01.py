from bfs_01 import INF, zero_one_bfs
import heapq
import random


def rand_graph(n, m, wlo=1, whi=9, directed=True):
    edges = []
    for _ in range(m):
        u, v = random.randrange(n), random.randrange(n)
        edges.append((u, v, random.randrange(wlo, whi + 1)))
    return edges


def to_adj(n, edges, directed=True):
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        if not directed:
            adj[v].append((u, w))
    return adj


def dijkstra(adj, s):
    dist = [INF] * len(adj)
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    return dist


def test_zero_one_bfs():
    for _ in range(100):
        n = random.randrange(1, 15)
        edges = rand_graph(n, random.randrange(0, 35), 0, 1)
        adj = to_adj(n, edges)
        assert zero_one_bfs(adj, 0) == dijkstra(adj, 0)
