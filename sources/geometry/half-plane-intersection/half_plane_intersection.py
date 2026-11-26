from collections import deque
from fractions import Fraction
from functools import cmp_to_key
def _div(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return Fraction(a, b)
    return a / b
def sgn(x):
    return (x > 0) - (x < 0)
def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])
def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]
def cross2(a, b):
    """Cross product of vectors a x b."""
    return a[0] * b[1] - a[1] * b[0]
def polygon_area2(poly):
    """Twice the signed area (positive for counter-clockwise polygons)."""
    return sum(cross2(poly[i], poly[(i + 1) % len(poly)]) for i in range(len(poly)))
def half_plane_intersection(planes, bound=10 ** 6):
    """planes: list of (p, d): the closed half-plane to the LEFT of the line
    through p with direction d. Returns the vertices (ccw) of the
    intersection clipped to [-bound, bound]^2, or [] if it has no area."""
    B = bound
    box = [((-B, -B), (1, 0)), ((B, -B), (0, 1)), ((B, B), (-1, 0)), ((-B, B), (0, -1))]
    def half(d):
        return 0 if (d[1] > 0 or (d[1] == 0 and d[0] > 0)) else 1
    def cmp(h1, h2):
        a, b = h1[1], h2[1]
        if half(a) != half(b):
            return half(a) - half(b)
        return -sgn(cross2(a, b))
    H = sorted(list(planes) + box, key=cmp_to_key(cmp))
    def inter(h1, h2):
        t = _div(cross2(sub(h2[0], h1[0]), h2[1]), cross2(h1[1], h2[1]))
        return (h1[0][0] + h1[1][0] * t, h1[0][1] + h1[1][1] * t)
    def out(h, pt):
        return cross2(h[1], sub(pt, h[0])) < 0
    dq = deque()
    for h in H:
        while len(dq) >= 2 and out(h, inter(dq[-1], dq[-2])):
            dq.pop()
        while len(dq) >= 2 and out(h, inter(dq[0], dq[1])):
            dq.popleft()
        if dq and cross2(h[1], dq[-1][1]) == 0:
            if dot(h[1], dq[-1][1]) < 0: return []
            if out(h, dq[-1][0]): dq.pop()
            else:
                continue
        dq.append(h)
    while len(dq) > 2 and out(dq[0], inter(dq[-1], dq[-2])):
        dq.pop()
    while len(dq) > 2 and out(dq[-1], inter(dq[0], dq[1])):
        dq.popleft()
    if len(dq) < 3: return []
    k = len(dq)
    if any(cross2(dq[i][1], dq[(i + 1) % k][1]) == 0 for i in range(k)):
        return []
    poly = [inter(dq[i], dq[(i + 1) % k]) for i in range(k)]
    poly = [p for i, p in enumerate(poly) if p != poly[i - 1]]
    if len(poly) < 3 or polygon_area2(poly) <= 0: return []
    return poly
