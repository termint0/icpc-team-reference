from two_sat import TwoSAT, scc
import itertools
import random
def reach(n, edges, s):
    adj = [[] for _ in range(n)]
    for u, v, *_ in edges:
        adj[u].append(v)
    seen, st = {s}, [s]
    while st:
        u = st.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                st.append(v)
    return seen

def test_scc():
    for _ in range(200):
        n = random.randrange(1, 10)
        adj = [[] for _ in range(n)]
        edges = []
        for _ in range(random.randrange(0, 20)):
            u, v = random.randrange(n), random.randrange(n)
            adj[u].append(v)
            edges.append((u, v))
        comp, k = scc(adj)
        R = [reach(n, edges, s) for s in range(n)]
        for u in range(n):
            for v in range(n):
                assert (comp[u] == comp[v]) == (v in R[u] and u in R[v])
        for u, v in edges:
            assert comp[u] >= comp[v]
        assert k == len(set(comp))

def test_two_sat():
    for _ in range(300):
        n = random.randrange(1, 6)
        clauses = [(random.randrange(2 * n), random.randrange(2 * n)) for _ in range(random.randrange(0, 12))]
        ts = TwoSAT(n)
        for a, b in clauses:
            ts.add_or(a, b)
        val = lambda asg, l: asg[l >> 1] ^ bool(l & 1)
        sat = any(all(val(asg, a) or val(asg, b) for a, b in clauses)
                  for asg in itertools.product([False, True], repeat=n))
        res = ts.solve()
        assert (res is not None) == sat
        if res:
            assert all(val(res, a) or val(res, b) for a, b in clauses)
    t = TwoSAT(2)
    t.add_implies(TwoSAT.lit(0), TwoSAT.lit(1, False))
    t.add_or(TwoSAT.lit(0), TwoSAT.lit(0))
    assert t.solve() == [True, False]
