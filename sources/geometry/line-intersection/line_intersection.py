from fractions import Fraction
def _div(a, b):
    if isinstance(a, int) and isinstance(b, int): return Fraction(a, b)
    return a / b

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def cross2(a, b):
    """Cross product of vectors a x b."""
    return a[0] * b[1] - a[1] * b[0]

def line_intersection(a, b, c, d):
    """Lines ab and cd. Returns (1, point), (0, None) if parallel and
    distinct, (-1, None) if they coincide."""
    r, s = sub(b, a), sub(d, c)
    den = cross2(r, s)
    if den == 0:
        return (-1, None) if cross2(sub(c, a), r) == 0 else (0, None)
    t = _div(cross2(sub(c, a), s), den)
    return 1, (a[0] + r[0] * t, a[1] + r[1] * t)
