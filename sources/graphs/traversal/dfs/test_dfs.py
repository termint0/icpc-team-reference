from dfs import dfs_order
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


def test_bfs_dfs():
    for _ in range(100):
        n = random.randrange(1, 15)
        adj = [[] for _ in range(n)]
        for _ in range(random.randrange(0, 30)):
            u, v = (random.randrange(n), random.randrange(n))
            adj[u].append(v)
            adj[v].append(u)
        pre, post, par = dfs_order(adj, 0)
        assert sorted(pre) == sorted(post) == sorted(reach(n, [(u, v) for u in range(n) for v in adj[u]], 0))
        pos = {v: i for i, v in enumerate(post)}
        for v in pre[1:]:
            assert pos[par[v]] > pos[v]
        assert pre[0] == 0 and par[0] == -1
