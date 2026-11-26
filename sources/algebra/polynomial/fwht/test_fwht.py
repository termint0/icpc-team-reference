from fwht import fwht, fwht_convolution
import random


def test_fwht():
    for mode, op in (("xor", lambda i, j: i ^ j), ("and", lambda i, j: i & j), ("or", lambda i, j: i | j)):
        for _ in range(30):
            b = random.randrange(0, 5)
            n = 1 << b
            x = [random.randrange(-5, 6) for _ in range(n)]
            y = [random.randrange(-5, 6) for _ in range(n)]
            exp = [0] * n
            for i in range(n):
                for j in range(n):
                    exp[op(i, j)] += x[i] * y[j]
            assert fwht_convolution(x, y, mode) == exp
            t = list(x)
            fwht(t, mode)
            fwht(t, mode, invert=True)
            assert t == x
