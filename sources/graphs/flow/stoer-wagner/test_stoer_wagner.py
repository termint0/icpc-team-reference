from stoer_wagner import stoer_wagner
import random


def test_stoer_wagner():
    for _ in range(100):
        n = random.randrange(2, 8)
        W = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i):
                W[i][j] = W[j][i] = random.choice([0, 0, 1, 2, 5])
        best = min(sum(W[i][j] for i in range(n) if m >> i & 1 for j in range(n) if not m >> j & 1)
                   for m in range(1, (1 << n) - 1))
        w, side = stoer_wagner(W)
        assert w == best
        assert 0 < len(side) < n
        S = set(side)
        assert sum(W[i][j] for i in S for j in range(n) if j not in S) == w
