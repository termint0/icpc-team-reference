def knapsack_01(weights, values, W):
    """Max value with total weight <= W, each item at most once. O(nW)."""
    dp = [0] * (W + 1)
    for w, v in zip(weights, values):
        for c in range(W, w - 1, -1):
            if dp[c - w] + v > dp[c]:
                dp[c] = dp[c - w] + v
    return dp[W]

def knapsack_unbounded(weights, values, W):
    """Each item may be used any number of times."""
    dp = [0] * (W + 1)
    for c in range(1, W + 1):
        for w, v in zip(weights, values):
            if w <= c and dp[c - w] + v > dp[c]:
                dp[c] = dp[c - w] + v
    return dp[W]

def knapsack_bounded(weights, values, counts, W):
    """Item i available counts[i] times; binary splitting, O(nW log c)."""
    ws, vs = [], []
    for w, v, c in zip(weights, values, counts):
        k = 1
        while c > 0:
            t = min(k, c)
            ws.append(w * t)
            vs.append(v * t)
            c -= t
            k <<= 1
    return knapsack_01(ws, vs, W)
