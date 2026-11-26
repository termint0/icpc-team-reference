from knapsack import knapsack_01, knapsack_bounded, knapsack_unbounded
import itertools
import random


def test_knapsacks():
    for _ in range(200):
        n = random.randrange(0, 7)
        w = [random.randrange(1, 8) for _ in range(n)]
        v = [random.randrange(0, 20) for _ in range(n)]
        c = [random.randrange(0, 4) for _ in range(n)]
        W = random.randrange(0, 20)
        b01 = max((sum(x for x, t in zip(v, m) if t) for m in itertools.product([0, 1], repeat=n)
                   if sum(x for x, t in zip(w, m) if t) <= W), default=0)
        assert knapsack_01(w, v, W) == b01
        bb = max((sum(x * k for x, k in zip(v, ks)) for ks in itertools.product(*[range(ci + 1) for ci in c])
                  if sum(x * k for x, k in zip(w, ks)) <= W), default=0)
        assert knapsack_bounded(w, v, c, W) == bb
        # unbounded = bounded with large counts
        assert knapsack_unbounded(w, v, W) == knapsack_bounded(w, v, [W + 1] * n, W)
