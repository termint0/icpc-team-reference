def ternary_search_float(f, lo, hi, iters=100):
    """Minimum of a unimodal function on [lo, hi]."""
    for _ in range(iters):
        m1, m2 = lo + (hi - lo) / 3, hi - (hi - lo) / 3
        if f(m1) < f(m2): hi = m2
        else: lo = m1
    return (lo + hi) / 2

def ternary_search_int(f, lo, hi):
    """argmin of a convex (or strictly unimodal) integer function on
    [lo, hi], by binary search on the slope. O(log n)."""
    while lo < hi:
        mid = (lo + hi) // 2
        if f(mid) <= f(mid + 1): hi = mid
        else: lo = mid + 1
    return lo
