def stoer_wagner(mat):
    """Global min cut of an undirected graph given as a symmetric weight
    matrix (zero diagonal), O(V^3). Returns (weight, vertices of one side)."""
    NEG = -(10 ** 18)
    mat = [row[:] for row in mat]
    n = len(mat)
    co = [[i] for i in range(n)]
    best = (float("inf"), [])
    for ph in range(1, n):
        w = mat[0][:]
        s = t = 0
        for _ in range(n - ph):
            w[t] = NEG
            s = t
            t = max(range(n), key=lambda i: w[i])
            for i in range(n):
                w[i] += mat[t][i]
        best = min(best, (w[t] - mat[t][t], co[t]), key=lambda x: x[0])
        co[s].extend(co[t])
        for i in range(n):
            mat[s][i] += mat[t][i]
        for i in range(n):
            mat[i][s] = mat[s][i]
        mat[0][t] = NEG
    return best
