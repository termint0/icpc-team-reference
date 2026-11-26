import random

from point_in_polygon import cross, point_in_polygon


def rp(lim):
    return (random.randint(-lim, lim), random.randint(-lim, lim))


def hull(pts):                      # monotone chain, only used to build convex test polygons
    P = sorted(set(pts))
    if len(P) < 3:
        return P
    lo, up = [], []
    for p in P:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    for p in reversed(P):
        while len(up) >= 2 and cross(up[-2], up[-1], p) <= 0:
            up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]


def test_concave_l_shape():
    L = [(0, 0), (4, 0), (4, 2), (2, 2), (2, 4), (0, 4)]
    expected = {(1, 1): 1, (3, 1): 1, (1, 3): 1, (3, 3): -1, (2, 2): 0, (4, 1): 0, (0, 0): 0,
                (5, 5): -1, (2, 3): 0, (-1, 1): -1}
    for p, v in expected.items():
        assert point_in_polygon(p, L) == v, p
        assert point_in_polygon(p, L[::-1]) == v, p      # orientation does not matter


def test_convex_polygons_against_half_plane_test():
    for _ in range(300):
        h = hull([rp(6) for _ in range(random.randrange(3, 12))])
        if len(h) < 3:
            continue
        for _ in range(20):
            p = rp(8)
            cs = [cross(h[i], h[(i + 1) % len(h)], p) for i in range(len(h))]
            exp = 1 if all(c > 0 for c in cs) else (0 if all(c >= 0 for c in cs) else -1)
            assert point_in_polygon(p, h) == exp
