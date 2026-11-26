from segment_tree_beats import SegTreeBeats
import random


def test_segtree_beats():
    for _ in range(60):
        n = random.randrange(1, 40)
        a = [random.randrange(-50, 100) for _ in range(n)]
        t = SegTreeBeats(a)
        for _ in range(100):
            l = random.randrange(n)
            r = random.randrange(l + 1, n + 1)
            op = random.random()
            if op < 0.4:
                x = random.randrange(-50, 100)
                for i in range(l, r):
                    a[i] = min(a[i], x)
                t.chmin(l, r, x)
            elif op < 0.7:
                assert t.sum(l, r) == sum(a[l:r])
            else:
                assert t.max(l, r) == max(a[l:r])
