from duval import duval
import random


def rs(n, alpha="ab"):
    return "".join(random.choice(alpha) for _ in range(n))


def test_duval_min_rotation():
    for _ in range(500):
        s = rs(random.randrange(1, 15), 'abc')
        f = [s[i:j] for i, j in duval(s)]
        assert ''.join(f) == s
        assert all((f[i] >= f[i + 1] for i in range(len(f) - 1)))
        for w in f:
            assert all((w < w[k:] for k in range(1, len(w))))
