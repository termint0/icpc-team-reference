from ordered_set import OrderedSet
import random


def test_ordered_set():
    for _ in range(10):
        s, ref = OrderedSet(), set()
        for _ in range(4000):
            x = random.randrange(0, 1500)
            op = random.random()
            if op < 0.5:
                assert s.insert(x) == (x not in ref)
                ref.add(x)
            elif op < 0.8:
                assert s.erase(x) == (x in ref)
                ref.discard(x)
            else:
                srt = sorted(ref)
                assert (x in s) == (x in ref)
                assert s.order_of_key(x) == sum(1 for y in srt if y < x)
                if srt:
                    k = random.randrange(len(srt))
                    assert s.find_by_order(k) == srt[k]
                exp = next((y for y in srt if y >= x), None)
                assert s.lower_bound(x) == exp
            assert len(s) == len(ref)
