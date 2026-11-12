def bip(adj):
    c = [-1] * len(adj)
    for s in range(len(adj)):
        if c[s] < 0:
            c[s] = 0; q = [s]
            for v in q:
                for u in adj[v]:
                    if c[u] < 0: c[u] = c[v] ^ 1; q.append(u)
                    elif c[u] == c[v]: return None
    return [v for v in range(len(adj)) if c[v] == 0], [v for v in range(len(adj)) if c[v] == 1]
