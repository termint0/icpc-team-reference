from link_cut_tree import LinkCutTree
import random


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


def test_link_cut_tree():
    for _ in range(30):
        n = random.randrange(2, 25)
        vals = [random.randrange(-9, 10) for _ in range(n)]
        lct = LinkCutTree(n, vals)
        adj = [set() for _ in range(n)]
        adjl = lambda: [list(s) for s in adj]
        for _ in range(250):
            op = random.random()
            u, v = random.randrange(n), random.randrange(n)
            def conn(a, b):
                seen, st = {a}, [a]
                while st:
                    x = st.pop()
                    for y in adj[x]:
                        if y not in seen:
                            seen.add(y)
                            st.append(y)
                return b in seen
            if op < 0.35:
                exp = u != v and not conn(u, v)
                assert lct.link(u, v) == (exp or (u != v and False))
                if exp:
                    adj[u].add(v)
                    adj[v].add(u)
            elif op < 0.55:
                has = v in adj[u]
                assert lct.cut(u, v) == has
                if has:
                    adj[u].discard(v)
                    adj[v].discard(u)
            elif op < 0.65:
                vals[u] = random.randrange(-9, 10)
                lct.set_value(u, vals[u])
            else:
                c = conn(u, v)
                assert lct.connected(u, v) == c
                if c:
                    assert lct.path_sum(u, v) == sum(vals[x] for x in path_nodes(adjl(), u, v))
