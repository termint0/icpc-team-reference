from matrix_exponentiation import mat_mul, mat_pow
import random


P = 1_000_000_007


def test_matrix_power():
    fib = mat_pow([[1, 1], [1, 0]], 90)
    assert fib[0][1] == 2880067194370816120
    for _ in range(50):
        n = random.randrange(1, 5)
        A = [[random.randrange(-5, 5) for _ in range(n)] for _ in range(n)]
        e = random.randrange(0, 8)
        R = [[int(i == j) for j in range(n)] for i in range(n)]
        for _ in range(e):
            R = mat_mul(R, A)
        assert mat_pow(A, e) == R
        assert mat_pow(A, e, 1000) == [[x % 1000 for x in row] for row in R]
    assert mat_pow([[1, 1], [1, 0]], 10**18, P)[0][1] == 209783453
