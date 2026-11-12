class Seg:  # monoid (op, e); default: sum. 0-indexed, point set, range query
    def __init__(s, n, op=lambda a, b: a + b, e=0):
        s.n, s.op, s.e = n, op, e
        s.t = [e] * (2 * n)

    def set(s, i, v):  # a[i] = v
        i += s.n; s.t[i] = v
        while i > 1: 
            i >>= 1 
            s.t[i] = s.op(s.t[2 * i], s.t[2 * i + 1])

    def query(s, l, r):  # op of a[l..r-1]
        a = b = s.e; l += s.n; r += s.n
        while l < r:
            if l & 1:
                a = s.op(a, s.t[l]); l += 1
            if r & 1:
                r -= 1
                b = s.op(s.t[r], b)
            l >>= 1; r >>= 1
        return s.op(a, b)
