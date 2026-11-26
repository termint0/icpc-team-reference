def solve_linear_mod(A, b, p):
    """Solve A x = b mod prime p. Return (x, rank) with free vars = 0, or
    None if inconsistent."""
    n, m = len(A), len(A[0])
    M = [[v % p for v in A[i]] + [b[i] % p] for i in range(n)]
    r = 0
    piv = []
    for c in range(m):
        sel = next((i for i in range(r, n) if M[i][c]), None)
        if sel is None:
            continue
        M[r], M[sel] = M[sel], M[r]
        inv = pow(M[r][c], p - 2, p)
        M[r] = [v * inv % p for v in M[r]]
        for i in range(n):
            if i != r and M[i][c]:
                f = M[i][c]
                M[i] = [(x - f * y) % p for x, y in zip(M[i], M[r])]
        piv.append(c)
        r += 1
    for i in range(r, n):
        if M[i][m]:
            return None
    x = [0] * m
    for i, c in enumerate(piv):
        x[c] = M[i][m]
    return x, r


def det_mod(A, p):
    n = len(A)
    M = [[v % p for v in row] for row in A]
    d = 1
    for c in range(n):
        sel = next((i for i in range(c, n) if M[i][c]), None)
        if sel is None:
            return 0
        if sel != c:
            M[c], M[sel] = M[sel], M[c]
            d = -d
        d = d * M[c][c] % p
        inv = pow(M[c][c], p - 2, p)
        for i in range(c + 1, n):
            if M[i][c]:
                f = M[i][c] * inv % p
                M[i] = [(x - f * y) % p for x, y in zip(M[i], M[c])]
    return d % p
