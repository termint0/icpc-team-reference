INF = float("inf")
def floyd_warshall(d):
    """d: n x n matrix (INF = no edge, d[i][i] = 0), modified in place.
    Pairs whose shortest path passes a negative cycle become -INF."""
    n = len(d)
    for k in range(n):
        dk = d[k]
        for i in range(n):
            dik = d[i][k]
            if dik == INF: continue
            di = d[i]
            for j in range(n):
                if dk[j] != INF and dik + dk[j] < di[j]:
                    di[j] = dik + dk[j]
    for k in range(n):
        if d[k][k] < 0:
            for i in range(n):
                for j in range(n):
                    if d[i][k] != INF and d[k][j] != INF:
                        d[i][j] = -INF
    return d
