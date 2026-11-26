def centroid_decomposition(adj):
    """Return (cpar, level): parent in the centroid tree (-1 for the root
    centroid) and its depth. Depth is <= log2(n)."""
    n = len(adj)
    removed = [False] * n
    cpar = [-1] * n
    level = [0] * n
    par = [-1] * n
    sz = [1] * n
    stack = [(0, -1, 0)]
    while stack:
        s, pc, lv = stack.pop()
        order = [s]
        par[s] = -1
        for u in order:
            sz[u] = 1
            for v in adj[u]:
                if v != par[u] and not removed[v]:
                    par[v] = u
                    order.append(v)
        for u in reversed(order):
            if par[u] != -1:
                sz[par[u]] += sz[u]
        total = len(order)
        c = s
        while True:
            for v in adj[c]:
                if v != par[c] and not removed[v] and sz[v] * 2 > total:
                    c = v
                    break
            else: break
        removed[c] = True
        cpar[c], level[c] = pc, lv
        for v in adj[c]:
            if not removed[v]: stack.append((v, c, lv + 1))
    return cpar, level
