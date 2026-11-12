class RangeUpdateRangeQuery:
    def __init__(s, n):
        s.b1 = BIT(n)  # d[k]
        s.b2 = BIT(n)  # k <*> d[k]
    def add(s, l, r, v):  # a[j] = a[j] <op> v for j in [l, r)
        s.b1.add(l, v)
        s.b2.add(l, l <*> v)
        s.b1.add(r, <inv>v)
        s.b2.add(r, r <*> <inv>v)
    def prefix(s, i):  # a[0] <op> ... <op> a[i-1]
        return (i <*> s.b1.sum(i)) <op> <inv>s.b2.sum(i)
    def rng(s, l, r):  # a[l] <op> ... <op> a[r-1]
        return s.prefix(r) <op> <inv>s.prefix(l)

