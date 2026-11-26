def lucas(n, k, p, binom=None):
    """C(n, k) mod small prime p, n and k huge."""
    if binom is None:
        binom = Binomial(p - 1, p)
    r = 1
    while n or k:
        ni, ki = n % p, k % p
        if ki > ni:
            return 0
        r = r * binom.C(ni, ki) % p
        n //= p
        k //= p
    return r
