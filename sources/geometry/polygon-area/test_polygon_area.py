from polygon_area import polygon_area2
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


def test_polygon_area_and_pip():
    sq = [(0, 0), (4, 0), (4, 4), (0, 4)]
    assert polygon_area2(sq) == 32 and polygon_area2(sq[::-1]) == -32
    L = [(0, 0), (4, 0), (4, 2), (2, 2), (2, 4), (0, 4)]
    assert polygon_area2(L) == 24
    for _ in range(300):
        pts = [rp(6) for _ in range(random.randrange(3, 12))]
        h = convex_hull(pts)
        if len(h) < 3:
            continue
