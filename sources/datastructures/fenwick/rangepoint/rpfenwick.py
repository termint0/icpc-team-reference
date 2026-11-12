class RangeUpdatePointQuery:
    def __init__(s, n):
        s.b = BIT(n)
    def add(s, l, r, v):  # a[j] = a[j] <op> v for j in [l, r)
        s.b.add(l, v)
        if r < s.b.n:
            s.b.add(r, <inv>v)
    def get(s, i):  # a[i]
        return s.b.sum(i + 1)
