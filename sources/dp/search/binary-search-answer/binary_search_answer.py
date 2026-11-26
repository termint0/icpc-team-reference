def first_true(lo, hi, pred):
    """Smallest x in [lo, hi) with pred(x) true, for monotone pred (false..
    false true..true). Returns hi if none."""
    while lo < hi:
        mid = (lo + hi) // 2
        if pred(mid): hi = mid
        else: lo = mid + 1
    return lo


def binary_search_float(lo, hi, pred, iters=100):
    """Boundary of a monotone predicate on reals (false -> true)."""
    for _ in range(iters):
        mid = (lo + hi) / 2
        if pred(mid): hi = mid
        else: lo = mid
    return hi
