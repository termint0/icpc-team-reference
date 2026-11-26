from xor_trie import XorTrie
import random


def test_tries():
    for _ in range(50):
        xt, ref = (XorTrie(10), [])
        for _ in range(80):
            x = random.randrange(1024)
            if random.random() < 0.6 or not ref:
                xt.insert(x)
                ref.append(x)
            elif random.random() < 0.5:
                y = random.choice(ref)
                xt.erase(y)
                ref.remove(y)
            if ref:
                assert xt.max_xor(x) == max((x ^ y for y in ref))
