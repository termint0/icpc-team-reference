def dc_optimization(n, K, cost):
    """dp[k][i] = min over j < i of dp[k-1][j] + cost(j, i), dp[0][0] = 0
    (split a[0:n] into K non-empty groups; cost(j, i) = cost of a[j:i]).
    Requires the monotone-opt (quadrangle) property. Returns dp[K][n]."""
    INF = float("inf")
    prev = [INF] * (n + 1)
    prev[0] = 0
    for _ in range(K):
        cur = [INF] * (n + 1)
        def rec(lo, hi, optlo, opthi):
            if lo > hi: return
            mid = (lo + hi) // 2
            best, bj = INF, -1
            for j in range(optlo, min(mid - 1, opthi) + 1):
                if prev[j] == INF: continue
                v = prev[j] + cost(j, mid)
                if v < best: best, bj = v, j
            cur[mid] = best
            if bj == -1: bj = optlo
            rec(lo, mid - 1, optlo, bj)
            rec(mid + 1, hi, bj, opthi)
        rec(1, n, 0, n - 1)
        prev = cur
    return prev[n]
