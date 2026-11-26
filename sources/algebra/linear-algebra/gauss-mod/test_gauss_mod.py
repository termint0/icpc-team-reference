from gauss_mod import det_mod, solve_linear_mod
import random


P = 1_000_000_007


def test_gauss_mod():
    p = 998244353
    for _ in range(200):
        n, m = random.randrange(1, 6), random.randrange(1, 6)
        A = [[random.randrange(0, 3) for _ in range(m)] for _ in range(n)]
        x0 = [random.randrange(0, p) for _ in range(m)]
        b = [sum(A[i][j] * x0[j] for j in range(m)) % p for i in range(n)]
        x, rk = solve_linear_mod(A, b, p)
        assert all(sum(A[i][j] * x[j] for j in range(m)) % p == b[i] for i in range(n))
    assert solve_linear_mod([[1, 1], [2, 2]], [1, 3], 7) is None
    assert solve_linear_mod([[1, 1], [2, 2]], [1, 2], 7)[1] == 1


def test_gauss_float_det():
    for _ in range(200):
        n = random.randrange(1, 6)
        A = [[random.uniform(-5, 5) for _ in range(n)] for _ in range(n)]
    for _ in range(100):
        n = random.randrange(1, 5)
        A = [[random.randrange(-4, 5) for _ in range(n)] for _ in range(n)]

        def det(M):
            if len(M) == 1:
                return M[0][0]
            return sum(((-1) ** j * M[0][j] * det([r[:j] + r[j + 1:] for r in M[1:]]) for j in range(len(M))))
        assert det_mod(A, P) == det(A) % P
