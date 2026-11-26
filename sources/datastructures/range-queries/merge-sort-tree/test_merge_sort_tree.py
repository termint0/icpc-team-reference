from merge_sort_tree import MergeSortTree
import random


def test_merge_sort_tree():
    for _ in range(50):
        n = random.randrange(1, 40)
        a = [random.randrange(10) for _ in range(n)]
        t = MergeSortTree(a)
        for _ in range(60):
            l = random.randrange(n + 1)
            r = random.randrange(l, n + 1)
            x = random.randrange(-1, 12)
            assert t.count_less(l, r, x) == sum(1 for v in a[l:r] if v < x)
