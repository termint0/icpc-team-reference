class SqrtDecomp:
    """Range add, range sum, point get in O(sqrt n)."""
    def __init__(self, a):
        self.n = len(a)
        self.B = max(1, int(self.n ** 0.5))
        self.a = list(a)
        nb = (self.n + self.B - 1) // self.B
        self.sm = [sum(self.a[i * self.B:(i + 1) * self.B]) for i in range(nb)]
        self.lz = [0] * nb

    def add(self, l, r, x):
        B = self.B
        while l < r and l % B:
            self.a[l] += x
            self.sm[l // B] += x
            l += 1
        while l + B <= r:
            self.lz[l // B] += x
            l += B
        while l < r:
            self.a[l] += x
            self.sm[l // B] += x
            l += 1

    def sum(self, l, r):
        B = self.B
        res = 0
        while l < r and l % B:
            res += self.a[l] + self.lz[l // B]
            l += 1
        while l + B <= r:
            res += self.sm[l // B] + self.lz[l // B] * B
            l += B
        while l < r:
            res += self.a[l] + self.lz[l // B]
            l += 1
        return res

    def get(self, i):
        return self.a[i] + self.lz[i // self.B]
