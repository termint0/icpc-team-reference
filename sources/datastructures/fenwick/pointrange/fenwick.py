class BIT:
    def __init__(s, n):
        s.n = n
        s.t = [<e>] * (n + 1)
    def build(s, a):  # a has length n
        for i in range(1, s.n + 1):
            s.t[i] = s.t[i] <op> a[i-1]
            j = i + (i & -i)
            if j <= s.n:
                s.t[j] = s.t[j] <op> s.t[i]
    def sum(s, i):  # a[0] <op> ... <op> a[i-1]
        r = <e>
        while i > 0:
            r = r <op> s.t[i]
            i -= i & -i
        return r
    def add(s, i, v):  # a[i] = a[i] <op> v
        i += 1
        while i <= s.n:
            s.t[i] = s.t[i] <op> v
            i += i & -i
