from edit_distance import edit_distance
import random


def test_lcs_edit():
    for _ in range(300):
        a = ''.join((random.choice('abc') for _ in range(random.randrange(0, 8))))
        b = ''.join((random.choice('abc') for _ in range(random.randrange(0, 8))))
        from functools import lru_cache

        @lru_cache(None)
        def ed(i, j):
            if i == len(a):
                return len(b) - j
            if j == len(b):
                return len(a) - i
            return min(ed(i + 1, j) + 1, ed(i, j + 1) + 1, ed(i + 1, j + 1) + (a[i] != b[j]))
        assert edit_distance(a, b) == ed(0, 0)
    assert edit_distance('kitten', 'sitting') == 3
