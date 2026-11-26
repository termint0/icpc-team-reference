from fractions import Fraction
from half_plane_intersection import cross2, half_plane_intersection, polygon_area2, sub
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


def clip(poly, h):
    p0, d = h
    out = []
    n = len(poly)
    for i in range(n):
        a, b = poly[i], poly[(i + 1) % n]
        sa, sb = cross2(d, sub(a, p0)), cross2(d, sub(b, p0))
        if sa >= 0:
            out.append(a)
        if (sa > 0 and sb < 0) or (sa < 0 and sb > 0):
            t = Fraction(sa) / (sa - sb)
            out.append((a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t))
    return out


def test_half_plane_intersection():
    B = 50
    for _ in range(600):
        planes = []
        for _ in range(random.randrange(1, 8)):
            p = rp(8)
            d = rp(4)
            if d == (0, 0):
                continue
            planes.append((p, d))
        poly = [(-B, -B), (B, -B), (B, B), (-B, B)]
        for h in planes:
            if poly:
                poly = clip(poly, h)
        area = Fraction(polygon_area2(poly), 2) if len(poly) >= 3 else 0
        got = half_plane_intersection(planes, B)
        if area == 0:
            assert got == [], (planes, got)
        else:
            assert Fraction(polygon_area2(got), 2) == area, (planes, got, poly)
            # same vertex set after removing collinear points of the clipper's output
            ref = {tuple(map(Fraction, p)) for p in convex_hull([(Fraction(x), Fraction(y)) for x, y in poly])}
            assert {tuple(map(Fraction, p)) for p in got} == ref
