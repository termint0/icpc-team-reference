from binomial_mod_p import Binomial
from math import comb
import random


P = 1_000_000_007


def test_binomial_lucas():
    B = Binomial(1000, P)
    for _ in range(300):
        n = random.randrange(0, 1001)
        k = random.randrange(-2, n + 3)
        assert B.C(n, k) == (comb(n, k) % P if 0 <= k <= n else 0)
    for p in (2, 3, 5, 7, 13):
        for _ in range(200):
            n, k = (random.randrange(0, 3000), random.randrange(0, 3000))
