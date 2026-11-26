from bisect import bisect_left
class MergeSortTree:
    """count_less(l, r, x): #{i in [l, r): a[i] < x} in O(log^2 n)."""
    def __init__(self, a):
        self.n = len(a)
        self.t = [[] for _ in range(2 * self.n)]
        for i, v in enumerate(a):
            self.t[self.n + i] = [v]
        for i in range(self.n - 1, 0, -1):
            self.t[i] = sorted(self.t[2 * i] + self.t[2 * i + 1])

    def count_less(self, l, r, x):
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                res += bisect_left(self.t[l], x)
                l += 1
            if r & 1:
                r -= 1
                res += bisect_left(self.t[r], x)
            l >>= 1
            r >>= 1
        return res
