class Binomial:
    """n! tables mod prime p; C(n, k) in O(1) for n <= N."""
    def __init__(self, N, p):
        self.p = p
        f = [1] * (N + 1)
        for i in range(1, N + 1):
            f[i] = f[i - 1] * i % p
        inv = [1] * (N + 1)
        inv[N] = pow(f[N], p - 2, p)
        for i in range(N, 0, -1):
            inv[i - 1] = inv[i] * i % p
        self.f, self.inv = f, inv

    def C(self, n, k):
        if k < 0 or k > n:
            return 0
        return self.f[n] * self.inv[k] % self.p * self.inv[n - k] % self.p
