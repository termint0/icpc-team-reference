from monotone_stack import largest_rectangle, next_greater, prev_smaller
import random


def test_monotone_helpers():
    for _ in range(100):
        n = random.randrange(1, 40)
        a = [random.randrange(-5, 10) for _ in range(n)]
        ng = next_greater(a)
        ps = prev_smaller(a)
        for i in range(n):
            exp = next((j for j in range(i + 1, n) if a[j] > a[i]), n)
            assert ng[i] == exp
            exp = next((j for j in range(i - 1, -1, -1) if a[j] < a[i]), -1)
            assert ps[i] == exp
        h = [abs(x) for x in a]
        brute = max((min(h[l:r]) * (r - l) for l in range(n) for r in range(l + 1, n + 1)))
        assert largest_rectangle(h) == brute
