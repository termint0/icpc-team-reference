from berlekamp_massey import berlekamp_massey
import random


P = 1_000_000_007


def test_berlekamp_massey():
    for _ in range(100):
        L = random.randrange(1, 6)
        c = [random.randrange(0, P) for _ in range(L)]
        s = [random.randrange(0, P) for _ in range(L)]
        while len(s) < 30:
            s.append(sum(c[i] * s[-1 - i] for i in range(L)) % P)
        rec = berlekamp_massey(s, P)
        assert len(rec) <= L
        for n in range(len(rec), len(s)):
            assert s[n] == sum(rec[i] * s[n - 1 - i] for i in range(len(rec))) % P
    fib = [0, 1]
    for _ in range(20):
        fib.append(fib[-1] + fib[-2])
    assert berlekamp_massey(fib, P) == [1, 1]
