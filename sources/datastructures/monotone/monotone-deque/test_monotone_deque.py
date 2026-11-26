from monotone_deque import sliding_window_min
import random


def test_monotone_helpers():
    for _ in range(100):
        n = random.randrange(1, 40)
        a = [random.randrange(-5, 10) for _ in range(n)]
        k = random.randrange(1, n + 1)
        assert sliding_window_min(a, k) == [min(a[i:i + k]) for i in range(n - k + 1)]
