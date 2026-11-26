from collections import deque
INF = float("inf")
class MinCostFlow:
    """Successive shortest paths with SPFA (negative costs OK, no negative
    cycles). O(F * V * E) worst case."""

    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.to, self.cap, self.cost = [], [], []

    def add_edge(self, u, v, cap, cost):
        self.adj[u].append(len(self.to))
        self.to.append(v)
        self.cap.append(cap)
        self.cost.append(cost)
        self.adj[v].append(len(self.to))
        self.to.append(u)
        self.cap.append(0)
        self.cost.append(-cost)

    def flow(self, s, t, maxf=INF):
        """Returns (flow, cost) of a min-cost flow of value <= maxf."""
        n, adj, to, cap, cost = self.n, self.adj, self.to, self.cap, self.cost
        total_f = total_c = 0
        while total_f < maxf:
            dist = [INF] * n
            inq = [False] * n
            pe = [-1] * n
            dist[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                inq[u] = False
                for e in adj[u]:
                    if cap[e] > 0 and dist[u] + cost[e] < dist[to[e]]:
                        v = to[e]
                        dist[v] = dist[u] + cost[e]
                        pe[v] = e
                        if not inq[v]:
                            inq[v] = True
                            q.append(v)
            if dist[t] == INF:
                break
            f, v = maxf - total_f, t
            while v != s:
                f = min(f, cap[pe[v]])
                v = to[pe[v] ^ 1]
            v = t
            while v != s:
                cap[pe[v]] -= f
                cap[pe[v] ^ 1] += f
                v = to[pe[v] ^ 1]
            total_f += f
            total_c += f * dist[t]
        return total_f, total_c
