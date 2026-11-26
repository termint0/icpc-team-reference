class MonotoneCHT:
    """Min-hull. Lines must be added with non-increasing slopes; queries are
    arbitrary (binary search)."""
    def __init__(self):
        self.k, self.m = [], []

    def add(self, k, m):
        K, M = self.k, self.m
        if K and K[-1] == k:
            if m >= M[-1]:
                return
            K.pop()
            M.pop()
        while len(K) >= 2 and (m - M[-2]) * (K[-2] - K[-1]) <= (M[-1] - M[-2]) * (K[-2] - k):
            K.pop()
            M.pop()
        K.append(k)
        M.append(m)

    def query(self, x):
        K, M = self.k, self.m
        lo, hi = 0, len(K) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if K[mid] * x + M[mid] > K[mid + 1] * x + M[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return K[lo] * x + M[lo]
