def cross(o, a, b):
    """(a - o) x (b - o): > 0 if o->a->b turns left (counter-clockwise)."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def dist2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def convex_diameter2(hull):
    """Squared diameter of a convex polygon (ccw hull) by rotating calipers."""
    n = len(hull)
    if n == 1: return 0
    if n == 2: return dist2(hull[0], hull[1])
    best, j = 0, 1
    for i in range(n):
        a, b = hull[i], hull[(i + 1) % n]
        while abs(cross(a, b, hull[(j + 1) % n])) > abs(cross(a, b, hull[j])):
            j = (j + 1) % n
        best = max(best, dist2(a, hull[j]), dist2(b, hull[j]))
    return best
