from ternary_search import ternary_search_float, ternary_search_int
import random


def test_mitm_and_search():
    for _ in range(100):
        c, w = (random.randrange(-50, 50), random.randrange(1, 5))
        f = lambda x: w * (x - c) ** 2
        assert ternary_search_int(f, -100, 100) == c
        assert abs(ternary_search_float(lambda x: (x - c / 7) ** 2, -100, 100) - c / 7) < 1e-06
    assert ternary_search_int(lambda x: abs(x), -5, 5) == 0
