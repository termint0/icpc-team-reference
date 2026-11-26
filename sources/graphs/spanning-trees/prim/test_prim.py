from prim import prim
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


def test_prim():
    for _ in range(200):
        n = random.randrange(1, 10)
        edges = rand_graph(n, random.randrange(0, 20), 1, 9)
        tot, par = prim(to_adj(n, edges, directed=False))
        p = list(range(n))

        def f(x):
            while p[x] != x:
                p[x] = p[p[x]]
                x = p[x]
            return x
        k = 0
        for u, v, w in sorted(edges, key=lambda e: e[2]):
            if f(u) != f(v):
                p[f(u)] = f(v)
                k += w
        assert tot == k
        assert par.count(-1) == len({f(v) for v in range(n)})
