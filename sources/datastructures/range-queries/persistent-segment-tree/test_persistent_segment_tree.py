from persistent_segment_tree import PersistentSegTree
import random


def test_persistent_segtree():
    n = 30
    for _ in range(30):
        pst = PersistentSegTree(n)
        roots, arrs = [0], [[0] * n]
        for _ in range(40):
            v = random.randrange(len(roots))
            pos, d = random.randrange(n), random.randrange(-5, 6)
            roots.append(pst.add(roots[v], pos, d))
            arr = arrs[v][:]
            arr[pos] += d
            arrs.append(arr)
        for _ in range(100):
            v = random.randrange(len(roots))
            l = random.randrange(n + 1)
            r = random.randrange(l, n + 1)
            assert pst.query(roots[v], l, r) == sum(arrs[v][l:r])
    # range k-th smallest via prefix versions
    a = [random.randrange(20) for _ in range(50)]
    pst = PersistentSegTree(20)
    pref = [0]
    for x in a:
        pref.append(pst.add(pref[-1], x, 1))
    for _ in range(200):
        l = random.randrange(50)
        r = random.randrange(l + 1, 51)
        k = random.randrange(r - l)
        assert pst.kth(pref[r], pref[l], k) == sorted(a[l:r])[k]
