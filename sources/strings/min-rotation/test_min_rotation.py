from min_rotation import min_rotation
import random


def rs(n, alpha="ab"):
    return "".join(random.choice(alpha) for _ in range(n))


def test_duval_min_rotation():
    for _ in range(500):
        s = rs(random.randrange(1, 15), 'abc')
        i = min_rotation(s)
        assert s[i:] + s[:i] == min((s[k:] + s[:k] for k in range(len(s))))
