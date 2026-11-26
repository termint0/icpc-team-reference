from min_cost_flow import MinCostFlow
import itertools
import random


def test_min_cost_flow():
    for _ in range(150):
        n = 4
        edges = []
        for _ in range(random.randrange(1, 7)):
            u, v = random.randrange(n - 1), random.randrange(1, n)
            if u < v:   # DAG => no negative cycles
                edges.append((u, v, random.randrange(1, 3), random.randrange(-3, 6)))
        mcf = MinCostFlow(n)
        for e in edges:
            mcf.add_edge(*e)
        got = mcf.flow(0, n - 1)
        best = None
        for fl in itertools.product(*[range(c + 1) for _, _, c, _ in edges]):
            bal = [0] * n
            for (u, v, _, _), f in zip(edges, fl):
                bal[u] -= f
                bal[v] += f
            if all(bal[i] == 0 for i in range(1, n - 1)):
                val = bal[n - 1]
                cost = sum(f * e[3] for e, f in zip(edges, fl))
                if best is None or (val, -cost) > (best[0], -best[1]):
                    best = (val, cost)
        assert got == (best[0], best[1]) or (best[0] == 0 and got[0] == 0)
    # assignment problem
    for _ in range(50):
        k = random.randrange(1, 5)
        C = [[random.randrange(-5, 20) for _ in range(k)] for _ in range(k)]
        mcf = MinCostFlow(2 * k + 2)
        for i in range(k):
            mcf.add_edge(2 * k, i, 1, 0)
            mcf.add_edge(k + i, 2 * k + 1, 1, 0)
            for j in range(k):
                mcf.add_edge(i, k + j, 1, C[i][j])
        f, c = mcf.flow(2 * k, 2 * k + 1)
        assert f == k and c == min(sum(C[i][p[i]] for i in range(k)) for p in itertools.permutations(range(k)))
