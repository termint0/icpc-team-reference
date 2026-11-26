import math
def sieve(n):
    """All primes <= n (Sieve of Eratosthenes)."""
    s = bytearray([1]) * (n + 1)
    for i in (0, 1):
        if i <= n: s[i] = 0
    for i in range(2, math.isqrt(n) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(range(i * i, n + 1, i)))
    return [i for i in range(n + 1) if s[i]]
