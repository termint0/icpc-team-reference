def mex(values):
    s = set(values)
    g = 0
    while g in s:
        g += 1
    return g

def grundy_table(N, options):
    """Grundy values g[0..N]. options(n, g) returns the Grundy values of the
    positions reachable from n, given the already known g[0..n-1]
    (XOR sub-games yourself, e.g. g[a] ^ g[b])."""
    g = []
    for n in range(N + 1):
        g.append(mex(options(n, g)))
    return g
