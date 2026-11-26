from miller_rabin import is_prime


def test_matches_trial_division_exhaustively():
    for n in range(0, 20000):
        exp = n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
        assert is_prime(n) == exp


def test_large_primes_and_pseudoprimes():
    assert is_prime(2 ** 61 - 1) and is_prime(1_000_000_007)
    assert not is_prime((2 ** 31 - 1) * (2 ** 61 - 1))
    # Carmichael numbers and strong pseudoprimes to many small bases
    for c in (561, 1105, 1729, 3215031751, 3825123056546413051):
        assert not is_prime(c)
