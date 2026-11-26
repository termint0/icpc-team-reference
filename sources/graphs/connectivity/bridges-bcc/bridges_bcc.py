def biconnected_components(n, edges):
    """edges: [(u, v)]. Returns (bridges, cut_vertices, blocks) where bridges
    is a list of edge ids, cut_vertices a sorted list, blocks a list of edge-id
    lists (one per biconnected component). Self-loops are ignored; parallel
    edges are handled."""
    adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        if u != v:
            adj[u].append((v, i))
            adj[v].append((u, i))
    tin = [-1] * n
    low = [0] * n
    it = [0] * n
    pe = [-1] * n
    timer = 0
    bridges, blocks, estack = [], [], []
    cut = [False] * n
    for root in range(n):
        if tin[root] != -1:
            continue
        tin[root] = low[root] = timer
        timer += 1
        stack = [root]
        root_children = 0
        while stack:
            u = stack[-1]
            if it[u] < len(adj[u]):
                v, eid = adj[u][it[u]]
                it[u] += 1
                if eid == pe[u]:
                    continue
                if tin[v] == -1:
                    pe[v] = eid
                    tin[v] = low[v] = timer
                    timer += 1
                    estack.append(eid)
                    stack.append(v)
                    if u == root:
                        root_children += 1
                elif tin[v] < tin[u]:
                    estack.append(eid)
                    low[u] = min(low[u], tin[v])
            else:
                stack.pop()
                if stack:
                    p = stack[-1]
                    low[p] = min(low[p], low[u])
                    if low[u] > tin[p]:
                        bridges.append(pe[u])
                    if low[u] >= tin[p]:
                        if p != root:
                            cut[p] = True
                        comp = []
                        while True:
                            e = estack.pop()
                            comp.append(e)
                            if e == pe[u]:
                                break
                        blocks.append(comp)
        if root_children >= 2:
            cut[root] = True
    return sorted(bridges), [v for v in range(n) if cut[v]], blocks
