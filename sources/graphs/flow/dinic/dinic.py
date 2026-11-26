class Dinic:
    """Max flow, O(V^2 E); O(E sqrt V) on unit networks."""
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.to, self.cap = [], []

    def add_edge(self, u, v, c, rc=0):
        """Edge u->v with capacity c (reverse capacity rc). Returns edge id."""
        self.adj[u].append(len(self.to))
        self.to.append(v)
        self.cap.append(c)
        self.adj[v].append(len(self.to))
        self.to.append(u)
        self.cap.append(rc)
        return len(self.to) - 2

    def max_flow(self, s, t):
        n, adj, to, cap = self.n, self.adj, self.to, self.cap
        flow = 0
        while True:
            level = [-1] * n
            level[s] = 0
            q = [s]
            for u in q:
                for e in adj[u]:
                    if cap[e] > 0 and level[to[e]] < 0:
                        level[to[e]] = level[u] + 1
                        q.append(to[e])
            if level[t] < 0:
                return flow
            it = [0] * n
            while True:
                path, u = [], s
                while u != t:
                    for i in range(it[u], len(adj[u])):
                        e = adj[u][i]
                        if cap[e] > 0 and level[to[e]] == level[u] + 1:
                            it[u] = i
                            path.append(e)
                            u = to[e]
                            break
                    else:
                        level[u] = -1  # dead end
                        if not path:
                            break
                        e = path.pop()
                        u = to[e ^ 1]
                        it[u] += 1
                if u != t:
                    break
                f = min(cap[e] for e in path)
                for e in path:
                    cap[e] -= f
                    cap[e ^ 1] += f
                flow += f

    def min_cut_side(self, s):
        """After max_flow: vertices on the source side of a minimum cut."""
        seen = [False] * self.n
        seen[s] = True
        st = [s]
        while st:
            u = st.pop()
            for e in self.adj[u]:
                if self.cap[e] > 0 and not seen[self.to[e]]:
                    seen[self.to[e]] = True
                    st.append(self.to[e])
        return seen
