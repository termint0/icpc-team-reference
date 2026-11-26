from burnside import necklaces
import itertools
import random


def test_inclusion_exclusion_burnside():
    for _ in range(200):
        n = random.randrange(1, 100)
    for n in range(1, 7):
        for k in range(1, 4):
            for flips in (False, True):
                seen = set()
                for col in itertools.product(range(k), repeat=n):
                    rots = [col[i:] + col[:i] for i in range(n)]
                    if flips:
                        rots += [t[::-1] for t in rots]
                    seen.add(min(rots))
                assert necklaces(n, k, flips) == len(seen)
    assert necklaces(6, 2) == 14 and necklaces(6, 2, True) == 13
