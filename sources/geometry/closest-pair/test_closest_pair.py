from closest_pair import closest_pair, dist2
import itertools
import random


def rp(lim=6):
    return (random.randint(-lim, lim), random.randint(-lim, lim))


def test_closest_pair():
    for _ in range(300):
        pts = [rp(12) for _ in range(random.randrange(2, 40))]
        d2, p, q = closest_pair(pts)
        assert d2 == min((dist2(a, b) for a, b in itertools.combinations(pts, 2)))
        assert dist2(p, q) == d2
