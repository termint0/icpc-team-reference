from min_enclosing_circle import _circumcenter, cross, min_enclosing_circle
import itertools
import math
import random


def rp(lim=6):
    return (random.randint(-lim, lim), random.randint(-lim, lim))


def brute_mec(pts):
    best = None
    cands = []
    for a, b in itertools.combinations(pts, 2):
        c = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
        cands.append((c, math.dist(c, a)))
    for a, b, c in itertools.combinations(pts, 3):
        if cross(a, b, c) != 0:
            o = _circumcenter(a, b, c)
            cands.append((o, math.dist(o, a)))
    for o, r in cands:
        if all(math.dist(o, p) <= r + 1e-9 for p in pts) and (best is None or r < best):
            best = r
    return best if best is not None else 0.0


def test_min_enclosing_circle():
    for _ in range(300):
        pts = [rp(9) for _ in range(random.randrange(1, 12))]
        c, r = min_enclosing_circle(pts)
        assert all(math.dist(c, p) <= r + 1e-7 for p in pts)
        assert abs(r - brute_mec(pts)) < 1e-6
    # 1000 collinear / cocircular points
    pts = [(i, 0) for i in range(1000)]
    assert abs(min_enclosing_circle(pts)[1] - 499.5) < 1e-6
