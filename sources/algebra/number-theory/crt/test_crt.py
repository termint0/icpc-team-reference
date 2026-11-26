from crt import crt, crt_list
from math import gcd
import random


def test_crt():
    for _ in range(2000):
        m1, m2 = random.randrange(1, 60), random.randrange(1, 60)
        a1, a2 = random.randrange(m1), random.randrange(m2)
        sol = [x for x in range(m1 * m2 // gcd(m1, m2)) if x % m1 == a1 and x % m2 == a2]
        r = crt(a1, m1, a2, m2)
        if sol:
            assert r == (sol[0], m1 * m2 // gcd(m1, m2))
        else:
            assert r is None
    assert crt_list([2, 3, 2], [3, 5, 7]) == (23, 105)
    assert crt_list([1, 0], [2, 4]) is None
