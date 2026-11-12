def LCA(adj, r=0):
    n = len(adj)
    t = [0] * n
    a = []
    s = [(r, -1, 0)]
    while s:
        v, p, d = s.pop()
        t[v] = len(a)
        a.append((d, p))
        s += [(u, v, d + 1) for u in adj[v] if u != p]
    m = len(a)
    T = [0] * m + a
    for i in range(m - 1, 0, -1):
        T[i] = min(T[2 * i], T[2 * i + 1])

    def lca(u, v):
        if u == v:
            return u
        l, r = sorted((t[u], t[v]))
        l += m + 1
        r += m + 1
        x = (n, n)
        while l < r:
            if l & 1:
                x = min(x, T[l])
                l += 1
            if r & 1:
                r -= 1
                x = min(x, T[r])
            l >>= 1
            r >>= 1
        return x[1]

    return lca
