class SegTree:
    """Needs an associative op with identity e (commutativity not required).
    Query is on the half-open range [l, r)."""

    def __init__(self, a, op, e):
        self.n, self.op, self.e = len(a), op, e
        self.t = [e] * self.n + list(a)
        for i in range(self.n - 1, 0, -1):
            self.t[i] = op(self.t[2 * i], self.t[2 * i + 1])

    def update(self, i, v):
        t, op = self.t, self.op
        i += self.n
        t[i] = v
        while i > 1:
            i >>= 1
            t[i] = op(t[2 * i], t[2 * i + 1])

    def query(self, l, r):
        t, op = self.t, self.op
        resl = resr = self.e
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                resl = op(resl, t[l])
                l += 1
            if r & 1:
                r -= 1
                resr = op(t[r], resr)
            l >>= 1
            r >>= 1
        return op(resl, resr)
