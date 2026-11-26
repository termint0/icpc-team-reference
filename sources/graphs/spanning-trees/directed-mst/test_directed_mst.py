from directed_mst import directed_mst
import itertools
import random


def rand_graph(n, m, wlo=1, whi=9, directed=True):
    edges = []
    for _ in range(m):
        u, v = random.randrange(n), random.randrange(n)
        edges.append((u, v, random.randrange(wlo, whi + 1)))
    return edges


def test_directed_mst():
    for _ in range(300):
        n = random.randrange(1, 6)
        edges = [e for e in rand_graph(n, random.randrange(0, 12), 1, 9) if e[0] != e[1]]
        root = 0
        best = None
        cand = [[(u, w) for u, v, w in edges if v == x] for x in range(n)]
        for choice in itertools.product(*[cand[x] if x != root else [(-1, 0)] for x in range(n)]):
            ok = True
            for x in range(n):
                y, steps = x, 0
                while y != root and steps <= n:
                    y = choice[y][0]
                    steps += 1
                if y != root:
                    ok = False
                    break
            if ok:
                c = sum(w for _, w in choice)
                if best is None or c < best:
                    best = c
        assert directed_mst(n, edges, root) == best
