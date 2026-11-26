from circle_intersection import circle_intersection
import math
import random


def test_circle_intersection():
    for _ in range(500):
        c1, c2 = (random.uniform(-5, 5), random.uniform(-5, 5)), (random.uniform(-5, 5), random.uniform(-5, 5))
        r1, r2 = random.uniform(0.1, 6), random.uniform(0.1, 6)
        res = circle_intersection(c1, r1, c2, r2)
        d = math.dist(c1, c2)
        if d > r1 + r2 or d < abs(r1 - r2):
            assert res == []
        else:
            assert len(res) == 2
            for p in res:
                assert abs(math.dist(p, c1) - r1) < 1e-7 and abs(math.dist(p, c2) - r2) < 1e-7
    assert circle_intersection((0, 0), 1, (2, 0), 1) == [(1.0, 0.0)]
    assert circle_intersection((0, 0), 1, (0, 0), 1) is None
    assert circle_intersection((0, 0), 1, (0, 0), 2) == []
