from euler_path import euler_path
import itertools
import random


def test_euler_path():
    for directed in (False, True):
        for _ in range(300):
            n = random.randrange(1, 6)
            edges = [(random.randrange(n), random.randrange(n)) for _ in range(random.randrange(0, 7))]
            res = euler_path(n, edges, directed)

            def key(a, b):
                return (a, b) if directed else (min(a, b), max(a, b))
            exists = False
            if not edges:
                exists = True
            else:
                for perm in itertools.permutations(range(len(edges))):
                    for flips in itertools.product([0, 1] if not directed else [0], repeat=len(edges)):
                        seq = []
                        for e, fl in zip(perm, flips):
                            u, v = edges[e]
                            seq.append((v, u) if fl else (u, v))
                        if all(seq[i][1] == seq[i + 1][0] for i in range(len(seq) - 1)):
                            exists = True
                            break
                    if exists:
                        break
            assert (res is not None) == exists, (edges, directed, res)
            if res is not None and edges:
                assert len(res) == len(edges) + 1
                used = sorted(key(res[i], res[i + 1]) for i in range(len(edges)))
                assert used == sorted(key(u, v) for u, v in edges)
