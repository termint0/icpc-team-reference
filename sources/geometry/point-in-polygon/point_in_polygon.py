def cross(o, a, b):
    """(a - o) x (b - o): > 0 if o->a->b turns left (counter-clockwise)."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def on_segment(a, b, p):
    """p lies on the closed segment ab."""
    return cross(a, b, p) == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) \
        and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])

def point_in_polygon(p, poly):
    """1 inside, 0 on the boundary, -1 outside (any simple polygon)."""
    inside = False
    n = len(poly)
    for i in range(n):
        a, b = poly[i], poly[(i + 1) % n]
        if on_segment(a, b, p):
            return 0
        if (a[1] > p[1]) != (b[1] > p[1]):
            c = cross(a, b, p)
            if (b[1] > a[1] and c > 0) or (b[1] < a[1] and c < 0):
                inside = not inside
    return 1 if inside else -1
