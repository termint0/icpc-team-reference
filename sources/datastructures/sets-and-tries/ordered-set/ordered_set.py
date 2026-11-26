from bisect import bisect_left, insort
class OrderedSet:
    """Sorted set with order_of_key / find_by_order, O(sqrt n) per op."""
    B = 256

    def __init__(self):
        self.blocks, self.maxes, self.n = [], [], 0

    def __len__(self):
        return self.n

    def _block(self, x):
        i = bisect_left(self.maxes, x)
        return min(i, len(self.blocks) - 1)

    def __contains__(self, x):
        if not self.blocks:
            return False
        b = self.blocks[self._block(x)]
        i = bisect_left(b, x)
        return i < len(b) and b[i] == x

    def insert(self, x):
        if x in self:
            return False
        if not self.blocks:
            self.blocks, self.maxes = [[x]], [x]
        else:
            i = self._block(x)
            insort(self.blocks[i], x)
            self.maxes[i] = self.blocks[i][-1]
            if len(self.blocks[i]) > 2 * self.B:
                b = self.blocks[i]
                self.blocks[i:i + 1] = [b[:self.B], b[self.B:]]
                self.maxes[i:i + 1] = [b[self.B - 1], b[-1]]
        self.n += 1
        return True

    def erase(self, x):
        if x not in self:
            return False
        i = self._block(x)
        b = self.blocks[i]
        del b[bisect_left(b, x)]
        if b:
            self.maxes[i] = b[-1]
        else:
            del self.blocks[i], self.maxes[i]
        self.n -= 1
        return True

    def order_of_key(self, x):
        """number of elements strictly less than x."""
        if not self.blocks:
            return 0
        i = self._block(x)
        return sum(len(b) for b in self.blocks[:i]) + bisect_left(self.blocks[i], x)

    def find_by_order(self, k):
        for b in self.blocks:
            if k < len(b):
                return b[k]
            k -= len(b)
        raise IndexError(k)

    def lower_bound(self, x):
        """smallest element >= x, or None."""
        k = self.order_of_key(x)
        return self.find_by_order(k) if k < self.n else None
