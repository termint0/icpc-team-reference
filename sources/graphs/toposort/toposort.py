def toposort(adj):
    deg = [0] * len(adj)
    for row in adj:
        for v in row: deg[v] += 1
    order = [i for i in range(len(adj)) if deg[i] == 0]
    for u in order:             # list grows as we iterate, so it acts as the queue
        for v in adj[u]:
            deg[v] -= 1
            if deg[v] == 0: order.append(v)
    return order if len(order) == len(adj) else None   # None = cycle
