def knuth_optimization(n, cost):
    """dp[i][j] = min_{i<k<j} dp[i][k] + dp[k][j] + cost(i, j), dp[i][i+1] = 0
    for the half-open interval [i, j). Needs the quadrangle inequality for
    cost. Returns dp[0][n]. O(n^2)."""
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    opt = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n): opt[i][i + 1] = i
    for length in range(2, n + 1):
        for i in range(0, n - length + 1):
            j = i + length
            best, bk = float("inf"), -1
            for k in range(max(opt[i][j - 1], i + 1), min(opt[i + 1][j], j - 1) + 1):
                v = dp[i][k] + dp[k][j]
                if v < best: best, bk = v, k
            dp[i][j] = best + cost(i, j)
            opt[i][j] = bk
    return dp[0][n]
