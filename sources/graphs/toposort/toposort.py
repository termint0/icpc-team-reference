def toposort(n, edges):
    g = [[] for _ in range(n)]
    deg = [0] * n
    for u, v in edges:          # edge u -> v means u comes before v
        g[u].append(v)
        deg[v] += 1
    order = [i for i in range(n) if deg[i] == 0]
    for u in order:             # list grows as we iterate, so it acts as the queue
        for v in g[u]:
            deg[v] -= 1
            if deg[v] == 0:
                order.append(v)
    return order if len(order) == n else None   # None means there's a cycle
