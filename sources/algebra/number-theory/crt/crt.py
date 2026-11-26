def ext_gcd(a, b):
    """Return (g, x, y) with a*x + b*y = g = gcd(a, b), a, b >= 0."""
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a - q * b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def crt(a1, m1, a2, m2):
    """Solve x = a1 (m1), x = a2 (m2). Return (x, lcm) or None."""
    g, x, _ = ext_gcd(m1, m2)
    if (a2 - a1) % g:
        return None
    l = m1 // g * m2
    t = (a2 - a1) // g * x % (m2 // g)
    return (a1 + m1 * t) % l, l

def crt_list(rems, mods):
    x, m = 0, 1
    for a, n in zip(rems, mods):
        r = crt(x, m, a % n, n)
        if r is None:
            return None
        x, m = r
    return x, m
