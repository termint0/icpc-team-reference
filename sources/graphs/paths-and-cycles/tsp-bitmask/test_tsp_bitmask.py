from tsp_bitmask import tsp
import itertools
import random


def test_tsp():
    for _ in range(40):
        n = random.randrange(1, 8)
        D = [[random.randrange(1, 20) for _ in range(n)] for _ in range(n)]
        cost, tour = tsp(D)
        if n == 1:
            assert cost == 0
            continue
        best = min(sum(D[a][b] for a, b in zip((0,) + p, p + (0,))) for p in itertools.permutations(range(1, n)))
        assert cost == best
        assert tour[0] == tour[-1] == 0 and sorted(tour[:-1]) == list(range(n))
        assert sum(D[a][b] for a, b in zip(tour, tour[1:])) == cost
