class LinkCutTree:
    """Dynamic forest with path-sum. Nodes are 0..n-1."""
    def __init__(self, n, vals=None):
        self.ch = [[0, 0] for _ in range(n + 1)]
        self.p = [0] * (n + 1)
        self.rev = [False] * (n + 1)
        self.val = [0] * (n + 1)
        self.sm = [0] * (n + 1)
        if vals:
            for i, v in enumerate(vals):
                self.val[i + 1] = self.sm[i + 1] = v

    def _is_root(self, x):
        p = self.p[x]
        return p == 0 or (self.ch[p][0] != x and self.ch[p][1] != x)

    def _push(self, x):
        if self.rev[x]:
            l, r = self.ch[x]
            self.ch[x] = [r, l]
            if l: self.rev[l] ^= True
            if r: self.rev[r] ^= True
            self.rev[x] = False

    def _pull(self, x):
        l, r = self.ch[x]
        self.sm[x] = self.sm[l] + self.sm[r] + self.val[x]

    def _rotate(self, x):
        p, ch = self.p, self.ch
        y = p[x]
        z = p[y]
        dx = 1 if ch[y][1] == x else 0
        if not self._is_root(y):
            ch[z][1 if ch[z][1] == y else 0] = x
        p[x] = z
        b = ch[x][dx ^ 1]
        ch[y][dx] = b
        if b: p[b] = y
        ch[x][dx ^ 1] = y
        p[y] = x
        self._pull(y)

    def _splay(self, x):
        st = [x]
        y = x
        while not self._is_root(y):
            y = self.p[y]
            st.append(y)
        for v in reversed(st): self._push(v)
        p, ch = self.p, self.ch
        while not self._is_root(x):
            y = p[x]
            if not self._is_root(y):
                z = p[y]
                self._rotate(y if (ch[y][0] == x) == (ch[z][0] == y) else x)
            self._rotate(x)
        self._pull(x)

    def _access(self, x):
        last = 0
        y = x
        while y:
            self._splay(y)
            self.ch[y][1] = last
            self._pull(y)
            last = y
            y = self.p[y]
        self._splay(x)

    def _make_root(self, x):
        self._access(x)
        self.rev[x] ^= True
        self._push(x)

    def _find_root(self, x):
        self._access(x)
        self._push(x)
        while self.ch[x][0]:
            x = self.ch[x][0]
            self._push(x)
        self._splay(x)
        return x

    def connected(self, u, v):
        u, v = u + 1, v + 1
        return u == v or self._find_root(u) == self._find_root(v)

    def link(self, u, v):
        """Add edge u-v; returns False if already connected."""
        u, v = u + 1, v + 1
        self._make_root(u)
        if self._find_root(v) == u: return False
        self.p[u] = v
        return True

    def cut(self, u, v):
        """Remove edge u-v; returns False if it does not exist."""
        u, v = u + 1, v + 1
        self._make_root(u)
        self._access(v)
        self._push(u)
        if self.ch[v][0] != u or self.ch[u][1]: return False
        self.ch[v][0] = 0
        self.p[u] = 0
        self._pull(v)
        return True

    def set_value(self, u, x):
        u += 1
        self._access(u)
        self.val[u] = x
        self._pull(u)

    def path_sum(self, u, v):
        """Sum of node values on the path u..v (they must be connected)."""
        u, v = u + 1, v + 1
        self._make_root(u)
        self._access(v)
        return self.sm[v]
