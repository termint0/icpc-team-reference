def solve_linear_float(A, b, eps=1e-9):
    """Gauss-Jordan with partial pivoting. Return (x, rank) or None."""
    n, m = len(A), len(A[0])
    M = [list(map(float, A[i])) + [float(b[i])] for i in range(n)]
    r = 0
    piv = []
    for c in range(m):
        sel = max(range(r, n), key=lambda i: abs(M[i][c]), default=None)
        if sel is None or abs(M[sel][c]) < eps:
            continue
        M[r], M[sel] = M[sel], M[r]
        d = M[r][c]
        M[r] = [v / d for v in M[r]]
        for i in range(n):
            if i != r and abs(M[i][c]) > 0:
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        piv.append(c)
        r += 1
    for i in range(r, n):
        if abs(M[i][m]) > eps:
            return None
    x = [0.0] * m
    for i, c in enumerate(piv):
        x[c] = M[i][m]
    return x, r
