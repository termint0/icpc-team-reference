class HLD:
    """adj: list of neighbour lists (tree). pos[v] is v's index in the
    decomposition order; each heavy path / subtree is a contiguous range."""
    def __init__(self, adj, root=0):
        n = len(adj)
        self.par = [-1] * n
        self.depth = [0] * n
        self.size = [1] * n
        self.heavy = [-1] * n
        self.head = [0] * n
        self.pos = [0] * n
        order = [root]
        for u in order:
            for v in adj[u]:
                if v != self.par[u]:
                    self.par[v] = u
                    self.depth[v] = self.depth[u] + 1
                    order.append(v)
        for u in reversed(order):
            p = self.par[u]
            if p != -1:
                self.size[p] += self.size[u]
                if self.heavy[p] == -1 or self.size[u] > self.size[self.heavy[p]]:
                    self.heavy[p] = u
        cur = 0
        stack = [root]
        self.head[root] = root
        while stack:
            h = stack.pop()
            v = h
            while v != -1:  # walk down heavy path starting at h
                self.head[v] = h
                self.pos[v] = cur
                cur += 1
                for w in adj[v]:
                    if w != self.par[v] and w != self.heavy[v]:
                        stack.append(w)
                v = self.heavy[v]

    def path(self, u, v):
        """Half-open position ranges [l, r) covering the path u..v (nodes)."""
        res = []
        while self.head[u] != self.head[v]:
            if self.depth[self.head[u]] < self.depth[self.head[v]]:
                u, v = v, u
            res.append((self.pos[self.head[u]], self.pos[u] + 1))
            u = self.par[self.head[u]]
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        res.append((self.pos[u], self.pos[v] + 1))
        return res

    def subtree(self, v):
        return self.pos[v], self.pos[v] + self.size[v]

    def lca(self, u, v):
        while self.head[u] != self.head[v]:
            if self.depth[self.head[u]] < self.depth[self.head[v]]:
                u, v = v, u
            u = self.par[self.head[u]]
        return u if self.depth[u] < self.depth[v] else v
