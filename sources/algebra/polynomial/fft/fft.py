import cmath; import math
def fft(a, invert=False):
    """In-place complex FFT; len(a) power of two."""
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j: a[i], a[j] = a[j], a[i]
    length = 2
    while length <= n:
        ang = 2 * math.pi / length * (-1 if invert else 1)
        wl = cmath.exp(1j * ang)
        half = length // 2
        ws = [1] * half
        for i in range(1, half):
            ws[i] = ws[i - 1] * wl
        for i in range(0, n, length):
            for k in range(half):
                u = a[i + k]
                v = a[i + k + half] * ws[k]
                a[i + k] = u + v
                a[i + k + half] = u - v
        length <<= 1
    if invert:
        for i in range(n): a[i] /= n
def convolution_fft(a, b):
    """Product of integer polynomials via complex FFT (rounded). Precise while
    result coefficients stay below ~1e14 / log(n)."""
    if not a or not b:
        return []
    need = len(a) + len(b) - 1
    sz = 1
    while sz < need: sz <<= 1
    fa = [complex(x) for x in a] + [0j] * (sz - len(a))
    fb = [complex(x) for x in b] + [0j] * (sz - len(b))
    fft(fa)
    fft(fb)
    for i in range(sz): fa[i] *= fb[i]
    fft(fa, True)
    return [round(fa[i].real) for i in range(need)]
