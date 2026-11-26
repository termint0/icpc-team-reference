from bisect import bisect_right
from collections import Counter
def meet_in_the_middle_count(a, target):
    """Number of subsets (by index) of a with sum == target. O(2^(n/2) n)."""
    def sums(arr):
        s = [0]
        for x in arr: s += [t + x for t in s]
        return s
    h = len(a) // 2
    left, right = sums(a[:h]), Counter(sums(a[h:]))
    return sum(right.get(target - s, 0) for s in left)

def closest_subset_sum(a, target):
    """Largest subset sum that is <= target (0 for the empty subset if all
    sums exceed it, so the answer may be > target only if empty sum is)."""
    def sums(arr):
        s = [0]
        for x in arr: s += [t + x for t in s]
        return s
    h = len(a) // 2
    left, right = sums(a[:h]), sorted(sums(a[h:]))
    best = None
    for s in left:
        i = bisect_right(right, target - s) - 1
        if i >= 0 and (best is None or s + right[i] > best):
            best = s + right[i]
    return best
