from spfa import INF, spfa
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


def reach(n, edges, s):
    adj = [[] for _ in range(n)]
    for u, v, *_ in edges:
        adj[u].append(v)
    seen, st = {s}, [s]
    while st:
        u = st.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                st.append(v)
    return seen


def ref_sssp(n, edges, s):
    """independent reference: plain FW with unbounded ints, then reachability."""
    D = [[INF] * n for _ in range(n)]
    for i in range(n):
        D[i][i] = 0
    for u, v, w in edges:
        D[u][v] = min(D[u][v], w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][k] != INF and D[k][j] != INF and D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
    neg = [c for c in range(n) if D[c][c] < 0 and c in reach(n, edges, s)]
    bad = set()
    for c in neg:
        bad |= reach(n, edges, c)
    return [(-INF if v in bad else D[s][v]) for v in range(n)], bool(neg)


def test_bellman_ford_spfa():
    for _ in range(300):
        n = random.randrange(1, 8)
        edges = rand_graph(n, random.randrange(0, 14), -4, 9)
        exp, has_neg = ref_sssp(n, edges, 0)
        res = spfa(to_adj(n, edges), 0)
        if has_neg:
            assert res is None
        else:
            assert res == exp
