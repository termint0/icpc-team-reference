from collections import Counter
from mo_algorithm import mo_algorithm
import random


def test_mo():
    for _ in range(30):
        n = random.randrange(1, 60)
        a = [random.randrange(6) for _ in range(n)]
        qs = []
        for _ in range(50):
            l = random.randrange(n)
            r = random.randrange(l + 1, n + 1)
            qs.append((l, r))
        cnt, distinct = Counter(), [0]

        def add(i):
            cnt[a[i]] += 1
            distinct[0] += cnt[a[i]] == 1

        def rem(i):
            cnt[a[i]] -= 1
            distinct[0] -= cnt[a[i]] == 0
        res = mo_algorithm(n, qs, add, rem, lambda: distinct[0])
        assert res == [len(set(a[l:r])) for l, r in qs]
