from linear_sieve import factor_spf, linear_sieve


def test_sieves():
    N = 5000
    naive = [i for i in range(2, N + 1) if all((i % d for d in range(2, int(i ** 0.5) + 1)))]
    primes, spf = linear_sieve(N)
    assert primes == naive
    for x in range(2, N + 1):
        f = factor_spf(x, spf)
        prod = 1
        for q in f:
            prod *= q
        assert prod == x and f == sorted(f)
