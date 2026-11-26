INF = float("inf")
def tsp(dist):
    """Min-cost Hamiltonian cycle through all nodes, O(2^n n^2).
    Returns (cost, tour starting and ending at 0)."""
    n = len(dist)
    if n == 1: return 0, [0, 0]
    full = 1 << n
    dp = [[INF] * n for _ in range(full)]
    par = [[-1] * n for _ in range(full)]
    dp[1][0] = 0
    for mask in range(1, full, 2):
        for last in range(n):
            c = dp[mask][last]
            if c == INF: continue
            for nx in range(1, n):
                if not mask >> nx & 1:
                    nm = mask | 1 << nx
                    if c + dist[last][nx] < dp[nm][nx]:
                        dp[nm][nx] = c + dist[last][nx]
                        par[nm][nx] = last
    best, bl = INF, -1
    for last in range(1, n):
        c = dp[full - 1][last] + dist[last][0]
        if c < best: best, bl = c, last
    if best == INF: return INF, []
    tour, mask, last = [], full - 1, bl
    while last != -1:
        tour.append(last)
        pl = par[mask][last]
        mask ^= 1 << last
        last = pl
    return best, tour[::-1] + [0]
