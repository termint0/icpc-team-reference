def sgn(x):
    return (x > 0) - (x < 0)

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]

def cross2(a, b):
    """Cross product of vectors a x b."""
    return a[0] * b[1] - a[1] * b[0]

def cross(o, a, b):
    """(a - o) x (b - o): > 0 if o->a->b turns left (counter-clockwise)."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def dist2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def on_segment(a, b, p):
    """p lies on the closed segment ab."""
    return cross(a, b, p) == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) \
        and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])
