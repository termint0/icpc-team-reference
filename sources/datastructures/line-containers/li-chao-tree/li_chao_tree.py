class LiChao:
    """Min of lines k*x+m at integer x in [lo, hi]. Lines in any order."""
    INF = float("inf")

    def __init__(self, lo, hi):
        self.lo, self.hi = lo, hi
        self.line, self.left, self.right = [None], [-1], [-1]

    @staticmethod
    def _f(ln, x):
        return ln[0] * x + ln[1]

    def add_line(self, k, m):
        node, lo, hi = 0, self.lo, self.hi
        new = (k, m)
        while True:
            cur = self.line[node]
            if cur is None:
                self.line[node] = new
                return
            mid = (lo + hi) // 2
            if self._f(new, mid) < self._f(cur, mid):
                self.line[node], new = new, cur
                cur = self.line[node]
            if lo == hi:
                return
            if self._f(new, lo) < self._f(cur, lo):
                nxt = "left"
                go = (lo, mid)
            elif self._f(new, hi) < self._f(cur, hi):
                nxt = "right"
                go = (mid + 1, hi)
            else:
                return
            side = self.left if nxt == "left" else self.right
            if side[node] == -1:
                side[node] = len(self.line)
                self.line.append(None)
                self.left.append(-1)
                self.right.append(-1)
            node = side[node]
            lo, hi = go

    def query(self, x):
        node, lo, hi, res = 0, self.lo, self.hi, self.INF
        while node != -1:
            if self.line[node] is not None:
                res = min(res, self._f(self.line[node], x))
            mid = (lo + hi) // 2
            if x <= mid:
                node, hi = self.left[node], mid
            else:
                node, lo = self.right[node], mid + 1
        return res
