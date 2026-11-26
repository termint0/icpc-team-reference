def linear_sieve(n):
    """Return (primes, spf) where spf[x] is the smallest prime factor of x."""
    spf = [0] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        for p in primes:
            if p > spf[i] or i * p > n:
                break
            spf[i * p] = p
    return primes, spf

def factor_spf(x, spf):
    """Prime factorisation (sorted with multiplicity) using an spf table."""
    f = []
    while x > 1:
        f.append(spf[x])
        x //= spf[x]
    return f
