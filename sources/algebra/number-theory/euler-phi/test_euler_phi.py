from euler_phi import euler_phi
from math import gcd


def test_phi():
    for n in range(1, 500):
        assert euler_phi(n) == sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)
