from fractions import Fraction
def _div(a, b):
    if isinstance(a, int) and isinstance(b, int): return Fraction(a, b)
    return a / b

def sgn(x):
    return (x > 0) - (x < 0)

def cross(o, a, b):
    """(a - o) x (b - o): > 0 if o->a->b turns left (counter-clockwise)."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def on_segment(a, b, p):
    """p lies on the closed segment ab."""
    return cross(a, b, p) == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) \
        and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])

def segment_intersection(a, b, c, d):
    """Intersection of closed segments ab and cd: a sorted list of 0, 1 or 2
    points (2 = collinear overlap, the endpoints of the overlap)."""
    oa, ob = cross(c, d, a), cross(c, d, b)
    oc, od = cross(a, b, c), cross(a, b, d)
    if sgn(oa) * sgn(ob) < 0 and sgn(oc) * sgn(od) < 0:
        t = _div(oa, oa - ob)
        return [(a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)]
    pts = set()
    if on_segment(c, d, a): pts.add(a)
    if on_segment(c, d, b): pts.add(b)
    if on_segment(a, b, c): pts.add(c)
    if on_segment(a, b, d): pts.add(d)
    return sorted(pts)
