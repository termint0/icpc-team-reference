NTT_MOD = 998244353
NTT_G = 3
def ntt(a, invert=False, mod=NTT_MOD, g=NTT_G):
    """In-place NTT; len(a) power of two dividing mod-1."""
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
        w = pow(g, (mod - 1) // length, mod)
        if invert: w = pow(w, mod - 2, mod)
        half = length // 2
        ws = [1] * half
        for i in range(1, half): ws[i] = ws[i - 1] * w % mod
        for i in range(0, n, length):
            for k in range(half):
                u = a[i + k]
                v = a[i + k + half] * ws[k] % mod
                a[i + k] = (u + v) % mod
                a[i + k + half] = (u - v) % mod
        length <<= 1
    if invert:
        ninv = pow(n, mod - 2, mod)
        for i in range(n): a[i] = a[i] * ninv % mod


def convolution_ntt(a, b, mod=NTT_MOD):
    """Polynomial product mod 998244353."""
    if not a or not b: return []
    need = len(a) + len(b) - 1
    sz = 1
    while sz < need: sz <<= 1
    fa = [x % mod for x in a] + [0] * (sz - len(a))
    fb = [x % mod for x in b] + [0] * (sz - len(b))
    ntt(fa, False, mod); ntt(fb, False, mod)
    for i in range(sz): fa[i] = fa[i] * fb[i] % mod
    ntt(fa, True, mod)
    return fa[:need]
