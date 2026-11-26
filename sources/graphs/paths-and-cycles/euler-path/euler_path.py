def euler_path(n, edges, directed=False):
    """Hierholzer. Returns the vertex sequence of an Euler path (a circuit if
    one exists), or None."""
    m = len(edges)
    adj = [[] for _ in range(n)]
    deg = [0] * n
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, i))
        if directed:
            deg[u] += 1
            deg[v] -= 1
        else:
            adj[v].append((u, i))
            deg[u] += 1
            deg[v] += 1
    start = next((v for v in range(n) if adj[v]), 0)
    if directed:
        pos = [v for v in range(n) if deg[v] == 1]
        neg = [v for v in range(n) if deg[v] == -1]
        if any(d not in (-1, 0, 1) for d in deg) or len(pos) != len(neg) or len(pos) > 1:
            return None
        if pos: start = pos[0]
    else:
        odd = [v for v in range(n) if deg[v] % 2]
        if len(odd) not in (0, 2): return None
        if odd: start = odd[0]
    used = [False] * m
    ptr = [0] * n
    stack, path = [start], []
    while stack:
        u = stack[-1]
        while ptr[u] < len(adj[u]) and used[adj[u][ptr[u]][1]]:
            ptr[u] += 1
        if ptr[u] == len(adj[u]):
            path.append(stack.pop())
        else:
            v, i = adj[u][ptr[u]]
            used[i] = True
            stack.append(v)
    if len(path) != m + 1: return None
    return path[::-1]
