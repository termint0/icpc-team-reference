from tree_diameter import tree_diameter
import heapq
import random

INF = float("inf")


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


def rand_tree(n):
    adj = [[] for _ in range(n)]
    for v in range(1, n):
        u = random.randrange(v)
        adj[u].append(v)
        adj[v].append(u)
    return adj


def test_tree_tools():
    for _ in range(60):
        n = random.randrange(1, 40)
        adj = rand_tree(n)
        for _ in range(50):
            u, v = (random.randrange(n), random.randrange(n))
        wadj = [[] for _ in range(n)]
        for u in range(n):
            for v in adj[u]:
                wadj[u].append((v, 1 + (u * 7 + v * 7) % 5))
        W = [dijkstra(wadj, s) for s in range(n)]
        length, path = tree_diameter(wadj)
        assert length == max((max(r) for r in W))
        assert W[path[0]][path[-1]] == length
