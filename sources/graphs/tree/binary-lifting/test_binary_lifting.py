from binary_lifting import BinaryLifting
from collections import deque
import random


def dfs_order(adj, s):
    """Iterative DFS. Returns (preorder, postorder, parent)."""
    n = len(adj)
    parent = [-2] * n
    parent[s] = -1
    pre, post, it, st = [s], [], [0] * n, [s]
    while st:
        u = st[-1]
        if it[u] < len(adj[u]):
            v = adj[u][it[u]]
            it[u] += 1
            if parent[v] == -2:
                parent[v] = u
                pre.append(v)
                st.append(v)
        else:
            post.append(st.pop())
    return pre, post, parent


INF = float("inf")


def bfs(adj, s):
    """Distances (in edges) from s; INF if unreachable."""
    dist = [INF] * len(adj)
    dist[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == INF:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


def rand_tree(n):
    adj = [[] for _ in range(n)]
    for v in range(1, n):
        u = random.randrange(v)
        adj[u].append(v)
        adj[v].append(u)
    return adj


def tree_dists(adj):
    return [bfs(adj, s) for s in range(len(adj))]


def test_tree_tools():
    for _ in range(60):
        n = random.randrange(1, 40)
        adj = rand_tree(n)
        D = tree_dists(adj)
        bl = BinaryLifting(adj, 0)
        pre, post, par = dfs_order(adj, 0)
        for _ in range(50):
            u, v = (random.randrange(n), random.randrange(n))
            assert bl.dist(u, v) == D[u][v]
            l = bl.lca(u, v)
            assert D[0][l] + D[l][u] == D[0][u] and D[0][l] + D[l][v] == D[0][v]
            k = random.randrange(0, 45)
            x = u
            for _ in range(k):
                x = par[x] if par[x] != -1 else x
            assert bl.kth_ancestor(u, k) == x
        wadj = [[] for _ in range(n)]
        for u in range(n):
            for v in adj[u]:
                wadj[u].append((v, 1 + (u * 7 + v * 7) % 5))
