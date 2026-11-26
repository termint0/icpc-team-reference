from lazy_segment_tree import LazySegTree
import random


def test_lazy_segtree_add_min_and_sum():
    INF = float("inf")
    for _ in range(60):
        n = random.randrange(1, 30)
        a = [random.randrange(-20, 20) for _ in range(n)]
        mn = LazySegTree(a, min, INF, lambda f, x: x + f, lambda f, g: f + g, 0)
        sm = LazySegTree([(v, 1) for v in a], lambda x, y: (x[0] + y[0], x[1] + y[1]), (0, 0),
                         lambda f, x: (x[0] + f * x[1], x[1]), lambda f, g: f + g, 0)
        for _ in range(80):
            l = random.randrange(n + 1)
            r = random.randrange(l, n + 1)
            if random.random() < 0.5:
                x = random.randrange(-5, 6)
                for i in range(l, r):
                    a[i] += x
                mn.update(l, r, x)
                sm.update(l, r, x)
            else:
                assert mn.query(l, r) == (min(a[l:r]) if l < r else INF)
                assert sm.query(l, r)[0] == sum(a[l:r])


def test_lazy_segtree_assign():
    # assignment with sentinel None as identity
    for _ in range(40):
        n = random.randrange(1, 25)
        a = [random.randrange(100) for _ in range(n)]
        t = LazySegTree([(v, 1) for v in a], lambda x, y: (x[0] + y[0], x[1] + y[1]), (0, 0),
                        lambda f, x: x if f is None else (f * x[1], x[1]),
                        lambda f, g: g if f is None else f, None)
        for _ in range(60):
            l = random.randrange(n + 1)
            r = random.randrange(l, n + 1)
            if random.random() < 0.5:
                v = random.randrange(100)
                a[l:r] = [v] * (r - l)
                t.update(l, r, v)
            else:
                assert t.query(l, r)[0] == sum(a[l:r])
