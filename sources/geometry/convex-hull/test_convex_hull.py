from convex_hull import convex_hull, cross
import random


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
    assert convex_hull([(0, 0)]) == [(0, 0)]
    assert convex_hull([(0, 0), (0, 0), (1, 1), (2, 2)]) == [(0, 0), (2, 2)]
