from inclusion_exclusion import count_coprime, count_divisible_by_any
import itertools
import math
import random


def test_inclusion_exclusion_burnside():
    for _ in range(200):
        nums = [random.randrange(2, 15) for _ in range(random.randrange(0, 5))]
        N = random.randrange(0, 300)
        assert count_divisible_by_any(N, nums) == sum((1 for x in range(1, N + 1) if any((x % d == 0 for d in nums))))
        n = random.randrange(1, 100)
        assert count_coprime(N, n) == sum((1 for x in range(1, N + 1) if math.gcd(x, n) == 1))
    assert count_divisible_by_any(10, [1, 3]) == 10
    for n in range(1, 7):
        for k in range(1, 4):
            for flips in (False, True):
                seen = set()
                for col in itertools.product(range(k), repeat=n):
                    rots = [col[i:] + col[:i] for i in range(n)]
                    if flips:
                        rots += [t[::-1] for t in rots]
                    seen.add(min(rots))
