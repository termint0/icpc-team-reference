from sieve import sieve


def test_sieves():
    N = 5000
    naive = [i for i in range(2, N + 1) if all((i % d for d in range(2, int(i ** 0.5) + 1)))]
    assert sieve(N) == naive
    assert sieve(1) == [] and sieve(2) == [2]
