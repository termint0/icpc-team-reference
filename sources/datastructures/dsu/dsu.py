class DSU:
    def __init__(s, n):
        s.p = list(range(n))
        s.sz = [1] * n

    def find(s, x):
        while s.p[x] != x:
            s.p[x] = s.p[s.p[x]]
            x = s.p[x]
        return x

    def union(s, a, b):
        a, b = s.find(a), s.find(b)
        if a == b: return False
        if s.sz[a] < s.sz[b]: a, b = b, a
        s.p[b] = a
        s.sz[a] += s.sz[b]
        return True
