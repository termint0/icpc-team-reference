def fwht(a, mode="xor", invert=False):
    """In-place fast Walsh-Hadamard transform (len a power of two).
    mode: 'xor', 'and' or 'or'. Exact for integers."""
    n = len(a); h = 1
    while h < n:
        for i in range(0, n, h * 2):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                if mode == "xor":
                    a[j], a[j + h] = x + y, x - y
                elif mode == "or":
                    a[j + h] = y + x if not invert else y - x
                else:  # and
                    a[j] = x + y if not invert else x - y
        h *= 2
    if invert and mode == "xor":
        for i in range(n): a[i] //= n
def fwht_convolution(a, b, mode="xor"):
    """c[k] = sum over i op j = k of a[i] * b[j] (sizes equal, power of 2)."""
    fa, fb = list(a), list(b)
    fwht(fa, mode); fwht(fb, mode)
    c = [x * y for x, y in zip(fa, fb)]
    fwht(c, mode, invert=True)
    return c
