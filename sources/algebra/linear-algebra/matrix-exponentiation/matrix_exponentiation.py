def mat_mul(A, B, mod=None):
    n, m, k = len(A), len(B), len(B[0])
    C = [[0] * k for _ in range(n)]
    for i in range(n):
        Ai, Ci = A[i], C[i]
        for t in range(m):
            a = Ai[t]
            if a:
                Bt = B[t]
                for j in range(k):
                    Ci[j] += a * Bt[j]
        if mod:
            for j in range(k):
                Ci[j] %= mod
    return C


def mat_pow(A, e, mod=None):
    n = len(A)
    R = [[int(i == j) for j in range(n)] for i in range(n)]
    while e:
        if e & 1:
            R = mat_mul(R, A, mod)
        A = mat_mul(A, A, mod)
        e >>= 1
    return R
