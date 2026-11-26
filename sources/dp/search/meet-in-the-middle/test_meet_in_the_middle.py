from meet_in_the_middle import closest_subset_sum, meet_in_the_middle_count
import itertools
import random


def test_mitm_and_search():
    for _ in range(200):
        a = [random.randrange(-6, 12) for _ in range(random.randrange(0, 11))]
        t = random.randrange(-10, 30)
        sums = [sum((x for x, k in zip(a, m) if k)) for m in itertools.product([0, 1], repeat=len(a))]
        assert meet_in_the_middle_count(a, t) == sums.count(t)
        le = [s for s in sums if s <= t]
        assert closest_subset_sum(a, t) == (max(le) if le else None)
    for _ in range(100):
        a = sorted((random.randrange(100) for _ in range(random.randrange(0, 15))))
