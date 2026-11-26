from permutations import kth_permutation, next_permutation, permutation_cycles, permutation_inverse, permutation_rank
import itertools
import random


def test_gray_perm():
    for n in range(0, 7):
        perms = list(itertools.permutations(range(n)))
        a, got = (list(range(n)), [])
        while True:
            got.append(tuple(a))
            if not next_permutation(a):
                break
        assert got == perms and a == list(range(n))
        for k in random.sample(range(len(perms)), min(10, len(perms))):
            assert tuple(kth_permutation(n, k)) == perms[k]
            assert permutation_rank(list(perms[k])) == k
        for p in perms[:30]:
            inv = permutation_inverse(list(p))
            assert all((inv[p[i]] == i for i in range(n)))
    assert permutation_cycles([1, 0, 3, 4, 2]) == [[0, 1], [2, 3, 4]]
