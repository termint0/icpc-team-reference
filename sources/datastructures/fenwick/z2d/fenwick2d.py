class BIT2:
    def __init__(s, n, m):
        s.n, s.m = n, m
        s.t = [[<e>] * (m + 1) for _ in range(n + 1)]
    def add(s, x, y, v):  # a[x][y] = a[x][y] <op> v
        x += 1
        while x <= s.n:
            j = y + 1
            while j <= s.m:
                s.t[x][j] = s.t[x][j] <op> v
                j += j & -j
            x += x & -x
    def sum(s, x, y):  # <op> of a[i][j] over rows [0,x), cols [0,y)
        r = <e>
        while x > 0:
            j = y
            while j > 0:
                r = r <op> s.t[x][j]
                j -= j & -j
            x -= x & -x
        return r
    def rng(s, x1, y1, x2, y2):  # [x1,x2) x [y1,y2)
            return (s.sum(x2, y2) <op> <inv>s.sum(x1, y2)) <op> (<inv>s.sum(x2, y1) <op> s.sum(x1, y1))
