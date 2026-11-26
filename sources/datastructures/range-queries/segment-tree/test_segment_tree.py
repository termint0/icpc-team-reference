from segment_tree import SegTree
import random


def test_segtree_noncommutative():
    for _ in range(100):
        n = random.randrange(1, 40)
        a = [random.choice("abcdef") for _ in range(n)]
        st = SegTree(a, lambda x, y: x + y, "")
        for _ in range(60):
            if random.random() < 0.3:
                i = random.randrange(n)
                a[i] = random.choice("xyz")
                st.update(i, a[i])
            l = random.randrange(n + 1)
            r = random.randrange(l, n + 1)
            assert st.query(l, r) == "".join(a[l:r])
