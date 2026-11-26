from kmp import kmp_search, prefix_function
import random


def sgn(x):
    return (x > 0) - (x < 0)


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def cross2(a, b):
    """Cross product of vectors a x b."""
    return a[0] * b[1] - a[1] * b[0]


def cross(o, a, b):
    """(a - o) x (b - o): > 0 if o->a->b turns left (counter-clockwise)."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def dist2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def on_segment(a, b, p):
    """p lies on the closed segment ab."""
    return cross(a, b, p) == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) \
        and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])


def rs(n, alpha="ab"):
    return "".join(random.choice(alpha) for _ in range(n))


def test_prefix_kmp_z():
    for _ in range(500):
        s = rs(random.randrange(0, 20))
        pi = prefix_function(s)
        for i in range(len(s)):
            sub = s[:i + 1]
            assert pi[i] == max((k for k in range(i + 1) if sub[:k] == sub[len(sub) - k:]), default=0)
        t, p = (rs(random.randrange(0, 30)), rs(random.randrange(1, 5)))
        assert kmp_search(t, p) == [i for i in range(len(t) - len(p) + 1) if t[i:i + len(p)] == p]
    assert kmp_search('aaaa', 'aa') == [0, 1, 2]
    assert kmp_search('abc', '') == [0, 1, 2, 3]
