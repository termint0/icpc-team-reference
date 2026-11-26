def blossom(n, adj):
    """Maximum matching in a general graph (Edmonds), O(V^3).
    Returns (size, match) with match[v] = partner or -1."""
    match = [-1] * n
    p = [-1] * n
    base = list(range(n))

    def lca(a, b):
        used = [False] * n
        while True:
            a = base[a]
            used[a] = True
            if match[a] == -1:
                break
            a = p[match[a]]
        while True:
            b = base[b]
            if used[b]:
                return b
            b = p[match[b]]

    def mark_path(v, b, child, blos):
        while base[v] != b:
            blos[base[v]] = blos[base[match[v]]] = True
            p[v] = child
            child = match[v]
            v = p[match[v]]

    def find_path(root):
        used = [False] * n
        for i in range(n):
            p[i] = -1
            base[i] = i
        used[root] = True
        q = [root]
        qh = 0
        while qh < len(q):
            v = q[qh]
            qh += 1
            for to in adj[v]:
                if base[v] == base[to] or match[v] == to:
                    continue
                if to == root or (match[to] != -1 and p[match[to]] != -1):
                    cb = lca(v, to)
                    blos = [False] * n
                    mark_path(v, cb, to, blos)
                    mark_path(to, cb, v, blos)
                    for i in range(n):
                        if blos[base[i]]:
                            base[i] = cb
                            if not used[i]:
                                used[i] = True
                                q.append(i)
                elif p[to] == -1:
                    p[to] = v
                    if match[to] == -1:
                        return to
                    used[match[to]] = True
                    q.append(match[to])
        return -1

    for i in range(n):
        if match[i] == -1:
            v = find_path(i)
            while v != -1:
                pv = p[v]
                ppv = match[pv]
                match[v], match[pv] = pv, v
                v = ppv
    return sum(1 for x in match if x != -1) // 2, match
