class PersistentSegTree:
    """Point add, range sum over positions [0, n). Every update returns a new
    root; root 0 is the all-zero version."""
    def __init__(self, n):
        self.n = n
        self.L, self.R, self.S = [0], [0], [0]

    def add(self, root, pos, delta):
        return self._add(root, 0, self.n, pos, delta)

    def _add(self, node, lo, hi, pos, delta):
        new = len(self.S)
        self.L.append(self.L[node])
        self.R.append(self.R[node])
        self.S.append(self.S[node] + delta)
        if hi - lo > 1:
            mid = (lo + hi) // 2
            if pos < mid:
                self.L[new] = self._add(self.L[node], lo, mid, pos, delta)
            else:
                self.R[new] = self._add(self.R[node], mid, hi, pos, delta)
        return new

    def query(self, root, l, r):
        return self._q(root, 0, self.n, l, r)

    def _q(self, node, lo, hi, l, r):
        if not node or r <= lo or hi <= l:
            return 0
        if l <= lo and hi <= r:
            return self.S[node]
        mid = (lo + hi) // 2
        return self._q(self.L[node], lo, mid, l, r) + self._q(self.R[node], mid, hi, l, r)

    def kth(self, ra, rb, k):
        """k-th smallest (0-indexed) position in multiset version ra minus
        version rb (e.g. ra = prefix r, rb = prefix l)."""
        lo, hi = 0, self.n
        while hi - lo > 1:
            mid = (lo + hi) // 2
            cnt = self.S[self.L[ra]] - self.S[self.L[rb]]
            if k < cnt:
                ra, rb, hi = self.L[ra], self.L[rb], mid
            else:
                k -= cnt
                ra, rb, lo = self.R[ra], self.R[rb], mid
        return lo
