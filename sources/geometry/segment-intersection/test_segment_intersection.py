from fractions import Fraction
from segment_intersection import segment_intersection
import random


def sgn(x):
    return (x > 0) - (x < 0)


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def cross2(a, b):
    """Cross product of vectors a x b."""
    return a[0] * b[1] - a[1] * b[0]


def cross(o, a, b):
    """(a - o) x (b - o): > 0 if o->a->b turns left (counter-clockwise)."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def dist2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def on_segment(a, b, p):
    """p lies on the closed segment ab."""
    return cross(a, b, p) == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) \
        and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])


def rp(lim=6):
    return (random.randint(-lim, lim), random.randint(-lim, lim))


def brute_seg_inter(a, b, c, d):
    r, s = sub(b, a), sub(d, c)
    den = cross2(r, s)
    if den != 0:
        t = Fraction(cross2(sub(c, a), s), den)
        u = Fraction(cross2(sub(c, a), r), den)
        if 0 <= t <= 1 and 0 <= u <= 1:
            return [(a[0] + r[0] * t, a[1] + r[1] * t)]
        return []
    if cross2(sub(c, a), r) != 0:
        return []
    # collinear: project onto the dominant axis of the direction
    ax = 0 if r[0] != 0 or s[0] != 0 else 1
    if a == b and c == d:
        return [a] if a == c else []
    key = lambda p: p[ax]
    lo = max(min(a, b, key=key), min(c, d, key=key), key=key)
    hi = min(max(a, b, key=key), max(c, d, key=key), key=key)
    if key(lo) > key(hi):
        return []
    return sorted({lo, hi})


def test_segment_intersection():
    for _ in range(3000):
        a, b, c, d = rp(4), rp(4), rp(4), rp(4)
        if a == b or c == d:
            continue
        got = segment_intersection(a, b, c, d)
        exp = brute_seg_inter(a, b, c, d)
        assert sorted((Fraction(x), Fraction(y)) for x, y in got) == sorted((Fraction(x), Fraction(y)) for x, y in exp), (a, b, c, d)
