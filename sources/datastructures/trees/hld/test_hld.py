from hld import HLD
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


def rand_tree(n, rng=random):
    adj = [[] for _ in range(n)]
    for v in range(1, n):
        u = rng.randrange(max(0, v - 5), v) if rng.random() < 0.5 else rng.randrange(v)
        adj[u].append(v)
        adj[v].append(u)
    return adj


def path_nodes(adj, u, v):
    par = {u: None}
    st = [u]
    while st:
        x = st.pop()
        for y in adj[x]:
            if y not in par:
                par[y] = x
                st.append(y)
    res = []
    while v is not None:
        res.append(v)
        v = par[v]
    return res


def test_hld():
    for _ in range(40):
        n = random.randrange(1, 60)
        adj = rand_tree(n)
        h = HLD(adj, 0)
        assert sorted(h.pos) == list(range(n))
        val = [random.randrange(-9, 10) for _ in range(n)]
        arr = [0] * n
        for v in range(n):
            arr[h.pos[v]] = val[v]
        for _ in range(50):
            u, v = random.randrange(n), random.randrange(n)
            p = path_nodes(adj, u, v)
            assert sum(sum(arr[l:r]) for l, r in h.path(u, v)) == sum(val[x] for x in p)
            assert h.depth[h.lca(u, v)] == min(h.depth[x] for x in p)
        for v in range(n):
            l, r = h.subtree(v)
            sub, st = set(), [v]
            while st:
                x = st.pop()
                sub.add(x)
                st += [y for y in adj[x] if y != h.par[x]]
            assert sorted(arr[l:r]) == sorted(val[x] for x in sub)
