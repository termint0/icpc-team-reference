INF = float("inf")
def directed_mst(n, edges, root):
    """Minimum arborescence (Chu-Liu/Edmonds), O(VE). edges = [(u, v, w)]
    directed u->v. Returns total cost or None if some vertex is unreachable."""
    res = 0
    while True:
        inw = [INF] * n
        pre = [-1] * n
        for u, v, w in edges:
            if u != v and w < inw[v]:
                inw[v] = w
                pre[v] = u
        for v in range(n):
            if v != root and inw[v] == INF: return None
        cnt = 0
        cid = [-1] * n
        vis = [-1] * n
        inw[root] = 0
        for v in range(n):
            res += inw[v]
            x = v
            while vis[x] != v and cid[x] == -1 and x != root:
                vis[x] = v
                x = pre[x]
            if x != root and cid[x] == -1:
                y = pre[x]
                while y != x:
                    cid[y] = cnt
                    y = pre[y]
                cid[x] = cnt
                cnt += 1
        if cnt == 0: return res
        for v in range(n):
            if cid[v] == -1:
                cid[v] = cnt
                cnt += 1
        edges = [(cid[u], cid[v], w - inw[v]) for u, v, w in edges if cid[u] != cid[v]]
        n, root = cnt, cid[root]
