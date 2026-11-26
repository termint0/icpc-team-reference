def assignment_bitmask(cost):
    """Min-cost assignment of n workers to n jobs by bitmask DP, O(2^n n)."""
    n = len(cost)
    INF = float("inf")
    dp = [INF] * (1 << n)
    dp[0] = 0
    for mask in range(1 << n):
        if dp[mask] == INF: continue
        i = bin(mask).count("1")
        if i == n: continue
        for j in range(n):
            if not mask >> j & 1:
                nm = mask | 1 << j
                if dp[mask] + cost[i][j] < dp[nm]:
                    dp[nm] = dp[mask] + cost[i][j]
    return dp[(1 << n) - 1]
