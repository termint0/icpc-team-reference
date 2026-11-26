from pollard_rho import factorize, is_prime
import random


def test_primality_and_factor():
    N = 20000
    for n in range(0, N):
        exp = n > 1 and all(n % d for d in range(2, int(n**.5) + 1))
        assert is_prime(n) == exp
    assert is_prime(2**61 - 1) and not is_prime((2**31 - 1) * (2**61 - 1))
    assert is_prime(1_000_000_007) and not is_prime(561) and not is_prime(3215031751)
    for _ in range(100):
        n = random.randrange(1, 10**12)
        f = factorize(n)
        prod = 1
        for q in f:
            assert is_prime(q)
            prod *= q
        assert prod == n
    big = (2**31 - 1) * (2**61 - 1)
    assert factorize(big) == [2**31 - 1, 2**61 - 1]
    assert factorize(1) == [] and factorize(2**10) == [2] * 10
