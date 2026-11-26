from line_intersection import cross2, line_intersection, sub
import random


def rp(lim=6):
    return (random.randint(-lim, lim), random.randint(-lim, lim))


def test_line_intersection():
    for _ in range(500):
        a, b, c, d = (rp(), rp(), rp(), rp())
        if a == b or c == d:
            continue
        st, p = line_intersection(a, b, c, d)
        den = cross2(sub(b, a), sub(d, c))
        if den != 0:
            assert st == 1
            assert cross2(sub(p, a), sub(b, a)) == 0 and cross2(sub(p, c), sub(d, c)) == 0
        elif cross2(sub(c, a), sub(b, a)) == 0:
            assert st == -1
        else:
            assert st == 0
