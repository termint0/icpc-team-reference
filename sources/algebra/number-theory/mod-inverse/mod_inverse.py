def ext_gcd(a, b):
    """Return (g, x, y) with a*x + b*y = g = gcd(a, b), a, b >= 0."""
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a - q * b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def mod_inv(a, m):
    """Inverse of a modulo m (any m, needs gcd(a, m) = 1)."""
    g, x, _ = ext_gcd(a % m, m)
    if g != 1:
        raise ValueError("inverse does not exist")
    return x % m
