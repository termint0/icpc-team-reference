def berlekamp_massey(s, p):
    """Shortest linear recurrence of s mod prime p.
    Returns c with s[n] = sum_{i=1..L} c[i-1] * s[n-i]."""
    C, B = [1], [1]
    L, m, b = 0, 1, 1
    for n in range(len(s)):
        d = s[n] % p
        for i in range(1, L + 1):
            d = (d + C[i] * s[n - i]) % p
        if d == 0:
            m += 1
            continue
        coef = d * pow(b, p - 2, p) % p
        T = C[:]
        if len(C) < len(B) + m:
            C = C + [0] * (len(B) + m - len(C))
        for i in range(len(B)):
            C[i + m] = (C[i + m] - coef * B[i]) % p
        if 2 * L <= n:
            L, B, b, m = n + 1 - L, T, d, 1
        else:
            m += 1
    C = C + [0] * (L + 1 - len(C))
    return [(-C[i]) % p for i in range(1, L + 1)]
