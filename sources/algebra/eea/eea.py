def eea(a, b):
    if b == 0: return a, 1, 0
    g, x, y = eea(b, a % b)
    return g, y, x - a//b*y
