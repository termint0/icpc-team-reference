from bitmask_dp import assignment_bitmask
import itertools
import random


def test_assignment_bitmask():
    for _ in range(100):
        n = random.randrange(1, 7)
        C = [[random.randrange(-5, 30) for _ in range(n)] for _ in range(n)]
        assert assignment_bitmask(C) == min(sum(C[i][p[i]] for i in range(n)) for p in itertools.permutations(range(n)))
