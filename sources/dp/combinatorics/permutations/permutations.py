import math
def next_permutation(a):
    """In-place lexicographic next permutation; returns False (and resets to
    sorted order) after the last one."""
    i = len(a) - 2
    while i >= 0 and a[i] >= a[i + 1]: i -= 1
    if i < 0:
        a.reverse()
        return False
    j = len(a) - 1
    while a[j] <= a[i]: j -= 1
    a[i], a[j] = a[j], a[i]
    a[i + 1:] = reversed(a[i + 1:])
    return True

def kth_permutation(n, k):
    """k-th (0-indexed) lexicographic permutation of 0..n-1. O(n^2)."""
    items = list(range(n))
    f = math.factorial(n - 1) if n else 1
    res = []
    for i in range(n, 0, -1):
        idx, k = divmod(k, f)
        res.append(items.pop(idx))
        if i > 1: f //= i - 1
    return res

def permutation_rank(p):
    """Lexicographic rank (0-indexed) of a permutation of 0..n-1. O(n^2)."""
    n, r = len(p), 0
    for i in range(n):
        smaller = sum(1 for j in range(i + 1, n) if p[j] < p[i])
        r += smaller * math.factorial(n - 1 - i)
    return r

def permutation_inverse(p):
    inv = [0] * len(p)
    for i, x in enumerate(p): inv[x] = i
    return inv

def permutation_cycles(p):
    seen, res = [False] * len(p), []
    for i in range(len(p)):
        if not seen[i]:
            cyc = []
            while not seen[i]:
                seen[i] = True
                cyc.append(i)
                i = p[i]
            res.append(cyc)
    return res
