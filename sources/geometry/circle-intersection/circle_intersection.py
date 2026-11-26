import math
def dist2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
def circle_intersection(c1, r1, c2, r2):
    """Intersection points of two circles (floats). Returns None if the
    circles coincide, else a list of 0, 1 or 2 points."""
    d2 = dist2(c1, c2)
    if d2 == 0:
        return None if r1 == r2 else []
    d = math.sqrt(d2)
    if d > r1 + r2 + 1e-12 or d < abs(r1 - r2) - 1e-12:
        return []
    a = (r1 * r1 - r2 * r2 + d2) / (2 * d)
    h2 = r1 * r1 - a * a
    h = math.sqrt(h2) if h2 > 0 else 0.0
    ux, uy = (c2[0] - c1[0]) / d, (c2[1] - c1[1]) / d
    mx, my = c1[0] + ux * a, c1[1] + uy * a
    if h == 0:
        return [(mx, my)]
    return [(mx - uy * h, my + ux * h), (mx + uy * h, my - ux * h)]
