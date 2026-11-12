def suffix_array(s):
    """sa[i] = start of the i-th smallest suffix."""
    n = len(s)
    if n == 0:
        return []
    ids = {c: i for i, c in enumerate(sorted(set(s)))}
    rank = [ids[c] for c in s]  # rank[i] < n always
    sa = list(range(n))
    k = 1
    while True:
        # key orders suffixes by their first 2k characters
        key = [rank[i] * (n + 1) + (rank[i + k] + 1 if i + k < n else 0)
               for i in range(n)]
        sa.sort(key=key.__getitem__)
        new = [0] * n
        for i in range(1, n):
            new[sa[i]] = new[sa[i - 1]] + (key[sa[i]] != key[sa[i - 1]])
        rank = new
        if rank[sa[-1]] == n - 1:  # all ranks distinct
            return sa
        k *= 2
