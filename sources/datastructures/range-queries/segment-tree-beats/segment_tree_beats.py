class SegTreeBeats:
    """Range chmin (a[i] = min(a[i], x)), range sum, range max. Amortised
    O((n + q) log n)."""
    NEG = -(10 ** 18)

    def __init__(self, a):
        n = self.n = len(a)
        self.mx = [0] * (4 * n)
        self.se = [self.NEG] * (4 * n)
        self.cnt = [0] * (4 * n)
        self.sm = [0] * (4 * n)
        if n:
            self._build(1, 0, n, a)

    def _pull(self, o):
        l, r = 2 * o, 2 * o + 1
        mx, se, cnt = self.mx, self.se, self.cnt
        self.sm[o] = self.sm[l] + self.sm[r]
        if mx[l] > mx[r]:
            mx[o], cnt[o], se[o] = mx[l], cnt[l], max(se[l], mx[r])
        elif mx[l] < mx[r]:
            mx[o], cnt[o], se[o] = mx[r], cnt[r], max(mx[l], se[r])
        else:
            mx[o], cnt[o], se[o] = mx[l], cnt[l] + cnt[r], max(se[l], se[r])

    def _build(self, o, l, r, a):
        if r - l == 1:
            self.mx[o], self.cnt[o], self.sm[o] = a[l], 1, a[l]
            return
        m = (l + r) // 2
        self._build(2 * o, l, m, a)
        self._build(2 * o + 1, m, r, a)
        self._pull(o)

    def _tag(self, o, x):
        if self.mx[o] > x:
            self.sm[o] -= (self.mx[o] - x) * self.cnt[o]
            self.mx[o] = x

    def _push(self, o):
        self._tag(2 * o, self.mx[o])
        self._tag(2 * o + 1, self.mx[o])

    def chmin(self, ql, qr, x, o=1, l=0, r=None):
        if r is None:
            r = self.n
        if qr <= l or r <= ql or self.mx[o] <= x:
            return
        if ql <= l and r <= qr and self.se[o] < x:
            self._tag(o, x)
            return
        self._push(o)
        m = (l + r) // 2
        self.chmin(ql, qr, x, 2 * o, l, m)
        self.chmin(ql, qr, x, 2 * o + 1, m, r)
        self._pull(o)

    def sum(self, ql, qr, o=1, l=0, r=None):
        if r is None:
            r = self.n
        if qr <= l or r <= ql:
            return 0
        if ql <= l and r <= qr:
            return self.sm[o]
        self._push(o)
        m = (l + r) // 2
        return self.sum(ql, qr, 2 * o, l, m) + self.sum(ql, qr, 2 * o + 1, m, r)

    def max(self, ql, qr, o=1, l=0, r=None):
        if r is None:
            r = self.n
        if qr <= l or r <= ql:
            return self.NEG
        if ql <= l and r <= qr:
            return self.mx[o]
        self._push(o)
        m = (l + r) // 2
        return max(self.max(ql, qr, 2 * o, l, m), self.max(ql, qr, 2 * o + 1, m, r))
