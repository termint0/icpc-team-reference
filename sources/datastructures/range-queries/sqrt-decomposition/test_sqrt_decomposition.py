from sqrt_decomposition import SqrtDecomp
import random


def test_sqrt_decomp():
    for _ in range(40):
        n = random.randrange(1, 70)
        a = [random.randrange(-9, 9) for _ in range(n)]
        s = SqrtDecomp(a)
        for _ in range(100):
            l = random.randrange(n + 1)
            r = random.randrange(l, n + 1)
            if random.random() < 0.5:
                x = random.randrange(-5, 6)
                for i in range(l, r):
                    a[i] += x
                s.add(l, r, x)
            else:
                assert s.sum(l, r) == sum(a[l:r])
        assert all(s.get(i) == a[i] for i in range(n))
