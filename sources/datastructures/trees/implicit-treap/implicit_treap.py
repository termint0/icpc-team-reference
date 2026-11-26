import random
class ImplicitTreap:
    """Sequence with insert/erase at index, range reverse, range sum."""
    def __init__(self, seed=12345):
        self.L, self.R, self.pri = [0], [0], [0]
        self.sz, self.val, self.sm, self.rev = [0], [0], [0], [False]
        self.root = 0
        self.rng = random.Random(seed)

    def __len__(self):
        return self.sz[self.root]

    def _new(self, v):
        self.L.append(0)
        self.R.append(0)
        self.pri.append(self.rng.random())
        self.sz.append(1)
        self.val.append(v)
        self.sm.append(v)
        self.rev.append(False)
        return len(self.sz) - 1

    def _upd(self, t):
        l, r = self.L[t], self.R[t]
        self.sz[t] = self.sz[l] + self.sz[r] + 1
        self.sm[t] = self.sm[l] + self.sm[r] + self.val[t]

    def _push(self, t):
        if self.rev[t]:
            l, r = self.L[t], self.R[t]
            self.L[t], self.R[t] = r, l
            if l: self.rev[l] ^= True
            if r: self.rev[r] ^= True
            self.rev[t] = False

    def _split(self, t, k):
        """first k elements -> left tree."""
        if not t:
            return 0, 0
        self._push(t)
        if self.sz[self.L[t]] >= k:
            a, b = self._split(self.L[t], k)
            self.L[t] = b
            self._upd(t)
            return a, t
        a, b = self._split(self.R[t], k - self.sz[self.L[t]] - 1)
        self.R[t] = a
        self._upd(t)
        return t, b

    def _merge(self, a, b):
        if not a or not b:
            return a or b
        if self.pri[a] > self.pri[b]:
            self._push(a)
            self.R[a] = self._merge(self.R[a], b)
            self._upd(a)
            return a
        self._push(b)
        self.L[b] = self._merge(a, self.L[b])
        self._upd(b)
        return b

    def insert(self, pos, v):
        a, b = self._split(self.root, pos)
        self.root = self._merge(self._merge(a, self._new(v)), b)

    def erase(self, pos):
        a, b = self._split(self.root, pos)
        m, c = self._split(b, 1)
        self.root = self._merge(a, c)
        return self.val[m]

    def reverse(self, l, r):
        a, b = self._split(self.root, l)
        m, c = self._split(b, r - l)
        if m:
            self.rev[m] ^= True
        self.root = self._merge(self._merge(a, m), c)

    def sum(self, l, r):
        a, b = self._split(self.root, l)
        m, c = self._split(b, r - l)
        res = self.sm[m]
        self.root = self._merge(self._merge(a, m), c)
        return res

    def to_list(self):
        out, st, t = [], [], self.root
        while st or t:
            while t:
                self._push(t)
                st.append(t)
                t = self.L[t]
            t = st.pop()
            out.append(self.val[t])
            t = self.R[t]
        return out
