def cross2(a, b):
    """Cross product of vectors a x b."""
    return a[0] * b[1] - a[1] * b[0]

def polygon_area2(poly):
    """Twice the signed area (positive for counter-clockwise polygons)."""
    return sum(cross2(poly[i], poly[(i + 1) % len(poly)]) for i in range(len(poly)))
