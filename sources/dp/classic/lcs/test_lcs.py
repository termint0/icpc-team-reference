from lcs import lcs
import itertools
import random


def is_subseq(s, t):
    it = iter(t)
    return all(c in it for c in s)


def test_lcs_edit():
    for _ in range(300):
        a = ''.join((random.choice('abc') for _ in range(random.randrange(0, 8))))
        b = ''.join((random.choice('abc') for _ in range(random.randrange(0, 8))))
        res = lcs(a, b)
        best = max((len(s) for r in range(len(a) + 1) for s in itertools.combinations(a, r) if is_subseq(s, b)))
        assert len(res) == best and is_subseq(res, a) and is_subseq(res, b)
        from functools import lru_cache

        @lru_cache(None)
        def ed(i, j):
            if i == len(a):
                return len(b) - j
            if j == len(b):
                return len(a) - i
            return min(ed(i + 1, j) + 1, ed(i, j + 1) + 1, ed(i + 1, j + 1) + (a[i] != b[j]))
