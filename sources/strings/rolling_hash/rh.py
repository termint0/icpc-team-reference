class RollingHash:
    MOD = (1 << 61) - 1

    def __init__(self, s, base=None):
        if base is None:
            base = random.randrange(256, self.MOD - 1)
        self.base = base
        vals = [ord(c) for c in s] if isinstance(s, str) else list(s)
        n = len(vals)
        self.h = [0] * (n + 1)
        self.pw = [1] * (n + 1)
        for i in range(n):
            self.h[i + 1] = (self.h[i] * base + vals[i]) % self.MOD
            self.pw[i + 1] = self.pw[i] * base % self.MOD

    def get(self, l, r):  # hash of s[l:r]
        return (self.h[r] - self.h[l] * self.pw[r - l]) % self.MOD
