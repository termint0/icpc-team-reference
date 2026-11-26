from implicit_treap import ImplicitTreap
import random


def test_implicit_treap():
    for _ in range(30):
        t, ref = ImplicitTreap(seed=random.randrange(10**9)), []
        for _ in range(200):
            op = random.random()
            if op < 0.4 or not ref:
                p = random.randrange(len(ref) + 1)
                v = random.randrange(-50, 50)
                t.insert(p, v)
                ref.insert(p, v)
            elif op < 0.55:
                p = random.randrange(len(ref))
                assert t.erase(p) == ref.pop(p)
            elif op < 0.8:
                l = random.randrange(len(ref) + 1)
                r = random.randrange(l, len(ref) + 1)
                t.reverse(l, r)
                ref[l:r] = ref[l:r][::-1]
            else:
                l = random.randrange(len(ref) + 1)
                r = random.randrange(l, len(ref) + 1)
                assert t.sum(l, r) == sum(ref[l:r])
            assert len(t) == len(ref)
        assert t.to_list() == ref
    t = ImplicitTreap()
    for i in range(2000):
        t.insert(i, i)  # large ordered input stays shallow
    assert t.to_list() == list(range(2000))
