def sos_subset_sum(a, bits):
    """f[mask] = sum of a[sub] over all sub subset of mask. O(2^b b)."""
    f = list(a)
    for b in range(bits):
        for mask in range(1 << bits):
            if mask >> b & 1:
                f[mask] += f[mask ^ (1 << b)]
    return f

def sos_superset_sum(a, bits):
    f = list(a)
    for b in range(bits):
        for mask in range(1 << bits):
            if not mask >> b & 1:
                f[mask] += f[mask | (1 << b)]
    return f

def sos_inverse(f, bits):
    """Inverse of sos_subset_sum (Moebius transform)."""
    a = list(f)
    for b in range(bits):
        for mask in range(1 << bits):
            if mask >> b & 1:
                a[mask] -= a[mask ^ (1 << b)]
    return a
