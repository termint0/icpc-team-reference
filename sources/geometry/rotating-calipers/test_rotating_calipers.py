from rotating_calipers import convex_diameter2, dist2
import random


def cross(o, a, b):
    """(a - o) x (b - o): > 0 if o->a->b turns left (counter-clockwise)."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def convex_hull(pts):
    """Andrew's monotone chain. Counter-clockwise hull without collinear
    points; duplicates are ignored."""
    P = sorted(set(pts))
    if len(P) <= 2:
        return P
    lo = []
    for p in P:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    up = []
    for p in reversed(P):
        while len(up) >= 2 and cross(up[-2], up[-1], p) <= 0:
            up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]


def rp(lim=6):
    return (random.randint(-lim, lim), random.randint(-lim, lim))


def test_convex_hull_area_diameter():
    for _ in range(300):
        pts = [rp(8) for _ in range(random.randrange(1, 15))]
        h = convex_hull(pts)
        hs = set(h)
        assert hs <= set(pts)
        n = len(h)
        if n >= 3:
            assert all((cross(h[i], h[(i + 1) % n], h[(i + 2) % n]) > 0 for i in range(n)))
        for p in pts:
            if n >= 3:
                assert all((cross(h[i], h[(i + 1) % n], p) >= 0 for i in range(n)))
        d2 = max((dist2(p, q) for p in pts for q in pts))
        assert convex_diameter2(h) == d2
    assert convex_hull([(0, 0)]) == [(0, 0)]
    assert convex_hull([(0, 0), (0, 0), (1, 1), (2, 2)]) == [(0, 0), (2, 2)]
