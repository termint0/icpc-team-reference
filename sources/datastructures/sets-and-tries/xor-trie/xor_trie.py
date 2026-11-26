class XorTrie:
    """Multiset of non-negative ints < 2^bits; max (x xor y) over stored y."""
    def __init__(self, bits=30):
        self.bits = bits
        self.ch = [[-1, -1]]
        self.cnt = [0]
    def _upd(self, x, d):
        v = 0
        for b in range(self.bits - 1, -1, -1):
            c = (x >> b) & 1
            if self.ch[v][c] == -1:
                self.ch[v][c] = len(self.ch)
                self.ch.append([-1, -1])
                self.cnt.append(0)
            v = self.ch[v][c]
            self.cnt[v] += d
    def insert(self, x):
        self._upd(x, 1)
    def erase(self, x):
        self._upd(x, -1)
    def max_xor(self, x):
        v, res = 0, 0
        for b in range(self.bits - 1, -1, -1):
            c = ((x >> b) & 1) ^ 1
            nv = self.ch[v][c]
            if nv != -1 and self.cnt[nv] > 0:
                res |= 1 << b
                v = nv
            else: v = self.ch[v][c ^ 1]
        return res
