import math

def catalan(n):
    return math.comb(2 * n, n) // (n + 1)

def stirling2_table(n):
    """S[i][j]: partitions of i elements into j non-empty blocks."""
    S = [[0] * (n + 1) for _ in range(n + 1)]
    S[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            S[i][j] = S[i - 1][j - 1] + j * S[i - 1][j]
    return S

def stirling1_table(n):
    """Unsigned Stirling numbers of the first kind: permutations of i
    elements with j cycles."""
    S = [[0] * (n + 1) for _ in range(n + 1)]
    S[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            S[i][j] = S[i - 1][j - 1] + (i - 1) * S[i - 1][j]
    return S

def bell(n):
    return sum(stirling2_table(n)[n])
