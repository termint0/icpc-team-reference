from gauss_float import solve_linear_float
import random


def test_gauss_float_det():
    for _ in range(200):
        n = random.randrange(1, 6)
        A = [[random.uniform(-5, 5) for _ in range(n)] for _ in range(n)]
        x0 = [random.uniform(-5, 5) for _ in range(n)]
        b = [sum((A[i][j] * x0[j] for j in range(n))) for i in range(n)]
        r = solve_linear_float(A, b, 1e-09)
        assert r is not None
        assert all((abs(u - v) < 1e-05 for u, v in zip(r[0], x0)))
    assert solve_linear_float([[1, 1], [1, 1]], [1, 2]) is None
    for _ in range(100):
        n = random.randrange(1, 5)
        A = [[random.randrange(-4, 5) for _ in range(n)] for _ in range(n)]

        def det(M):
            if len(M) == 1:
                return M[0][0]
            return sum(((-1) ** j * M[0][j] * det([r[:j] + r[j + 1:] for r in M[1:]]) for j in range(len(M))))
