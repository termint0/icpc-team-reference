from lis import lis
import itertools
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


def test_lis():
    for _ in range(500):
        a = [random.randrange(6) for _ in range(random.randrange(0, 12))]
        for strict in (True, False):
            idx = lis(a, strict)
            ok = (lambda x, y: x < y) if strict else (lambda x, y: x <= y)
            assert all(i < j and ok(a[i], a[j]) for i, j in zip(idx, idx[1:]))
            best = 0
            for r in range(len(a) + 1):
                for sub in itertools.combinations(range(len(a)), r):
                    if all(ok(a[i], a[j]) for i, j in zip(sub, sub[1:])):
                        best = max(best, r)
            assert len(idx) == best
