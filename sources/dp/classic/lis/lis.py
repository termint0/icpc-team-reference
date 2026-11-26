from bisect import bisect_left, bisect_right
def lis(a, strict=True):
    """Longest (strictly, or non-decreasing) increasing subsequence in
    O(n log n). Returns the list of indices of one optimal subsequence."""
    tails, tail_idx = [], []
    prev = [-1] * len(a)
    find = bisect_left if strict else bisect_right
    for i, x in enumerate(a):
        k = find(tails, x)
        if k == len(tails):
            tails.append(x)
            tail_idx.append(i)
        else:
            tails[k] = x
            tail_idx[k] = i
        prev[i] = tail_idx[k - 1] if k else -1
    res = []
    i = tail_idx[-1] if tail_idx else -1
    while i != -1:
        res.append(i)
        i = prev[i]
    return res[::-1]
