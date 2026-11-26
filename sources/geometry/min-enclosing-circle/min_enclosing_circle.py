import math
import random
def cross(o, a, b):
    """(a - o) x (b - o): > 0 if o->a->b turns left (counter-clockwise)."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def dist2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def _circumcenter(a, b, c):
    bx, by = b[0] - a[0], b[1] - a[1]
    cx, cy = c[0] - a[0], c[1] - a[1]
    d = 2 * (bx * cy - by * cx)
    ux = (cy * (bx * bx + by * by) - by * (cx * cx + cy * cy)) / d
    uy = (bx * (cx * cx + cy * cy) - cx * (bx * bx + by * by)) / d
    return (a[0] + ux, a[1] + uy)

def min_enclosing_circle(pts, eps=1e-9):
    """Welzl-style randomised incremental algorithm, expected O(n).
    Returns (centre, radius)."""
    P = list(pts)
    random.shuffle(P)
    c, r2 = (float(P[0][0]), float(P[0][1])), 0.0
    for i in range(len(P)):
        if dist2(c, P[i]) > r2 * (1 + eps) + eps:
            c, r2 = (float(P[i][0]), float(P[i][1])), 0.0
            for j in range(i):
                if dist2(c, P[j]) > r2 * (1 + eps) + eps:
                    c = ((P[i][0] + P[j][0]) / 2, (P[i][1] + P[j][1]) / 2)
                    r2 = dist2(c, P[i])
                    for k in range(j):
                        if dist2(c, P[k]) > r2 * (1 + eps) + eps:
                            if cross(P[i], P[j], P[k]) == 0:  # collinear: widest pair
                                trio = [P[i], P[j], P[k]]
                                u, v = max(((x, y) for x in trio for y in trio),
                                           key=lambda xy: dist2(*xy))
                                c = ((u[0] + v[0]) / 2, (u[1] + v[1]) / 2)
                            else:
                                c = _circumcenter(P[i], P[j], P[k])
                            r2 = dist2(c, P[i])
    return c, math.sqrt(r2)
