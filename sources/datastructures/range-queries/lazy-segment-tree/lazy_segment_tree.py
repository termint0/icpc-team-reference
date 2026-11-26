class LazySegTree:
    """Range-apply, range-query. Monoid (op, e) on values; monoid of maps
    (composition(f, g) = f after g, id_), with mapping(f, x) = f applied to x.
    Half-open ranges [l, r)."""

    def __init__(self, a, op, e, mapping, composition, id_):
        self.n = len(a)
        self.op, self.e, self.mp, self.comp, self.id = op, e, mapping, composition, id_
        self.d = [e] * (4 * self.n)
        self.lz = [id_] * (4 * self.n)
        if self.n:
            self._build(1, 0, self.n, a)

    def _build(self, o, l, r, a):
        if r - l == 1:
            self.d[o] = a[l]
            return
        m = (l + r) // 2
        self._build(2 * o, l, m, a)
        self._build(2 * o + 1, m, r, a)
        self.d[o] = self.op(self.d[2 * o], self.d[2 * o + 1])

    def _apply(self, o, f):
        self.d[o] = self.mp(f, self.d[o])
        self.lz[o] = self.comp(f, self.lz[o])

    def _push(self, o):
        self._apply(2 * o, self.lz[o])
        self._apply(2 * o + 1, self.lz[o])
        self.lz[o] = self.id

    def update(self, ql, qr, f, o=1, l=0, r=None):
        if r is None:
            r = self.n
        if qr <= l or r <= ql:
            return
        if ql <= l and r <= qr:
            self._apply(o, f)
            return
        self._push(o)
        m = (l + r) // 2
        self.update(ql, qr, f, 2 * o, l, m)
        self.update(ql, qr, f, 2 * o + 1, m, r)
        self.d[o] = self.op(self.d[2 * o], self.d[2 * o + 1])

    def query(self, ql, qr, o=1, l=0, r=None):
        if r is None:
            r = self.n
        if qr <= l or r <= ql:
            return self.e
        if ql <= l and r <= qr:
            return self.d[o]
        self._push(o)
        m = (l + r) // 2
        return self.op(self.query(ql, qr, 2 * o, l, m), self.query(ql, qr, 2 * o + 1, m, r))
