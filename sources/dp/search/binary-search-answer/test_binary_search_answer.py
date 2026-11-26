from binary_search_answer import binary_search_float, first_true
import math
import random


def test_mitm_and_search():
    for _ in range(200):
        a = [random.randrange(-6, 12) for _ in range(random.randrange(0, 11))]
    for _ in range(100):
        a = sorted((random.randrange(100) for _ in range(random.randrange(0, 15))))
        x = random.randrange(-5, 105)
        assert first_true(0, len(a), lambda i: a[i] >= x) == next((i for i in range(len(a)) if a[i] >= x), len(a))
        assert abs(binary_search_float(0, 100, lambda v: v * v >= 2) - math.sqrt(2)) < 1e-09
