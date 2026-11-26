class BinaryLifting:
    """k-th ancestor and LCA in O(log n) after O(n log n) build."""
    def __init__(self, adj, root=0):
        n = len(adj)
        self.LOG = max(1, n.bit_length())
        self.depth = [0] * n
        up0 = [root] * n
        order, seen = [root], [False] * n
        seen[root] = True
        for u in order:
            for v in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    up0[v] = u
                    self.depth[v] = self.depth[u] + 1
                    order.append(v)
        self.up = [up0]
        for j in range(1, self.LOG):
            prev = self.up[-1]
            self.up.append([prev[prev[v]] for v in range(n)])
    def kth_ancestor(self, v, k):
        """k-th ancestor; the root if k exceeds the depth."""
        k = min(k, self.depth[v])
        for j in range(self.LOG):
            if k >> j & 1: v = self.up[j][v]
        return v
    def lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        u = self.kth_ancestor(u, self.depth[u] - self.depth[v])
        if u == v: return u
        for j in range(self.LOG - 1, -1, -1):
            if self.up[j][u] != self.up[j][v]:
                u, v = self.up[j][u], self.up[j][v]
        return self.up[0][u]

    def dist(self, u, v):
        return self.depth[u] + self.depth[v] - 2 * self.depth[self.lca(u, v)]
