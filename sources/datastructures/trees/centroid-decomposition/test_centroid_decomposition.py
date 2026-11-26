from centroid_decomposition import centroid_decomposition
import random


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


def test_centroid_decomposition():
    for _ in range(40):
        n = random.randrange(1, 80)
        adj = rand_tree(n)
        cpar, lvl = centroid_decomposition(adj)
        assert cpar.count(-1) == 1
        assert max(lvl) <= max(n, 1).bit_length()
        for _ in range(30):
            u, v = random.randrange(n), random.randrange(n)
            anc = set()
            x = u
            while x != -1:
                anc.add(x)
                x = cpar[x]
            x = v
            while x not in anc:
                x = cpar[x]
            # centroid-LCA lies on the u-v path
            assert x in path_nodes(adj, u, v)
