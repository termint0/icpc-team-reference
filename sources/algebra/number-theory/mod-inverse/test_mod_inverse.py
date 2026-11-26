from math import gcd
from mod_inverse import ext_gcd, mod_inv
import random


def test_mod_pow_inv():
    for _ in range(300):
        b, e, m = (random.randrange(0, 10 ** 9), random.randrange(0, 10 ** 6), random.randrange(1, 10 ** 9))
    for _ in range(300):
        m = random.randrange(2, 10 ** 6)
        a = random.randrange(1, m)
        if gcd(a, m) == 1:
            assert a * mod_inv(a, m) % m == 1
        else:
            try:
                mod_inv(a, m)
                assert False
            except ValueError:
                pass


def test_ext_gcd():
    for _ in range(500):
        a, b = random.randrange(0, 10**9), random.randrange(0, 10**9)
        g, x, y = ext_gcd(a, b)
        assert g == gcd(a, b) and a * x + b * y == g
