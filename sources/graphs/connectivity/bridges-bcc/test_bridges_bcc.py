from bridges_bcc import biconnected_components
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


def comps_after_removal(n, edges, skip_e=None, skip_v=None):
    p = list(range(n))

    def f(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x
    for i, (u, v) in enumerate(edges):
        if i == skip_e or u == skip_v or v == skip_v:
            continue
        p[f(u)] = f(v)
    return len({f(v) for v in range(n) if v != skip_v})


def test_biconnected():
    for _ in range(300):
        n = random.randrange(1, 9)
        edges = [(random.randrange(n), random.randrange(n)) for _ in range(random.randrange(0, 13))]
        bridges, cuts, blocks = biconnected_components(n, edges)
        base = comps_after_removal(n, edges)
        assert bridges == [i for i, (u, v) in enumerate(edges)
                           if u != v and comps_after_removal(n, edges, skip_e=i) > base]
        deg = [0] * n
        for u, v in edges:
            if u != v:
                deg[u] += 1
                deg[v] += 1
        exp_cuts = [v for v in range(n) if comps_after_removal(n, edges, skip_v=v) > base - (1 if deg[v] == 0 else 0)]
        assert cuts == exp_cuts
        all_e = sorted(e for b in blocks for e in b)
        assert all_e == [i for i, (u, v) in enumerate(edges) if u != v]
        # blocks: 2-vertex-connected (or a single edge), block-cut tree identity
        verts = []
        for b in blocks:
            vs = sorted({x for e in b for x in edges[e]})
            verts.append(vs)
            if len(vs) > 2:
                for r in vs:
                    rest = [vv for vv in vs if vv != r]
                    sub = [edges[e] for e in b if r not in edges[e]]
                    idx = {vv: i for i, vv in enumerate(rest)}
                    sub = [(idx[u], idx[v]) for u, v in sub]
                    assert comps_after_removal(len(rest), sub) == 1
        occur = [0] * n
        for vs in verts:
            for x in vs:
                occur[x] += 1
        assert [v for v in range(n) if occur[v] >= 2] == exp_cuts
        # per-component: sum(|V(b)|-1) == |V|-1
        p = list(range(n))

        def f(x):
            while p[x] != x:
                p[x] = p[p[x]]
                x = p[x]
            return x
        for u, v in edges:
            p[f(u)] = f(v)
        for r in {f(v) for v in range(n) if deg[v] > 0}:
            size = sum(1 for v in range(n) if f(v) == r)
            assert sum(len(vs) - 1 for vs in verts if f(vs[0]) == r) == size - 1
    # path graph of 100k nodes: no recursion limit
    n = 100000
    b, c, bl = biconnected_components(n, [(i, i + 1) for i in range(n - 1)])
    assert len(b) == n - 1 and len(c) == n - 2 and len(bl) == n - 1
