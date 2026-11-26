from bfs import INF, bfs
import random


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


def test_bfs_dfs():
    for _ in range(100):
        n = random.randrange(1, 15)
        adj = [[] for _ in range(n)]
        for _ in range(random.randrange(0, 30)):
            u, v = (random.randrange(n), random.randrange(n))
            adj[u].append(v)
            adj[v].append(u)
        d = bfs(adj, 0)
        ref = ref_sssp(n, [(u, v, 1) for u in range(n) for v in adj[u]], 0)[0]
        assert d == ref
