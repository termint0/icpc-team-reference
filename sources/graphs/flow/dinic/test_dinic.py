from collections import deque
from dinic import Dinic
import random

INF = float("inf")


def rand_graph(n, m, wlo=1, whi=9, directed=True):
    edges = []
    for _ in range(m):
        u, v = random.randrange(n), random.randrange(n)
        edges.append((u, v, random.randrange(wlo, whi + 1)))
    return edges


def edmonds_karp(n, edges, s, t):
    cap = [[0] * n for _ in range(n)]
    for u, v, c in edges:
        cap[u][v] += c
    flow = 0
    while True:
        par = [-1] * n
        par[s] = s
        q = deque([s])
        while q and par[t] == -1:
            u = q.popleft()
            for v in range(n):
                if cap[u][v] > 0 and par[v] == -1:
                    par[v] = u
                    q.append(v)
        if par[t] == -1:
            return flow
        f, v = INF, t
        while v != s:
            f = min(f, cap[par[v]][v])
            v = par[v]
        v = t
        while v != s:
            cap[par[v]][v] -= f
            cap[v][par[v]] += f
            v = par[v]
        flow += f


def test_dinic_and_mincut():
    for _ in range(200):
        n = random.randrange(2, 9)
        edges = rand_graph(n, random.randrange(0, 20), 1, 10)
        d = Dinic(n)
        for u, v, c in edges:
            d.add_edge(u, v, c)
        f = d.max_flow(0, n - 1)
        assert f == edmonds_karp(n, edges, 0, n - 1)
        side = d.min_cut_side(0)
        assert side[0] and not side[n - 1]
        assert sum(c for u, v, c in edges if side[u] and not side[v]) == f
    # long path, check no recursion issues
    n = 20000
    d = Dinic(n)
    for i in range(n - 1):
        d.add_edge(i, i + 1, 5)
    assert d.max_flow(0, n - 1) == 5
