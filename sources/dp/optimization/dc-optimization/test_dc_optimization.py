from dc_optimization import dc_optimization
import random


def test_dc_and_knuth():
    for _ in range(100):
        n = random.randrange(1, 12)
        K = random.randrange(1, n + 1)
        a = [random.randrange(0, 10) for _ in range(n)]
        pre = [0]
        for x in a:
            pre.append(pre[-1] + x)
        cost = lambda j, i: (pre[i] - pre[j]) ** 2
        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(K + 1)]
        dp[0][0] = 0
        for k in range(1, K + 1):
            for i in range(1, n + 1):
                dp[k][i] = min((dp[k - 1][j] + cost(j, i) for j in range(i)))
        assert dc_optimization(n, K, cost) == dp[K][n]
        m = random.randrange(1, 14)
        s = [random.randrange(1, 10) for _ in range(m)]
        ps = [0]
        for x in s:
            ps.append(ps[-1] + x)
        c = lambda i, j: ps[j] - ps[i]
        from functools import lru_cache

        @lru_cache(None)
        def f(i, j):
            if j - i == 1:
                return 0
            return min((f(i, k) + f(k, j) for k in range(i + 1, j))) + c(i, j)
