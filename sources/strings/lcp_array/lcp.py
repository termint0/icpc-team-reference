def lcp_array(s, sa):
    """lcp[i] = longest common prefix of suffixes sa[i], sa[i+1]."""
    n = len(s)
    rank = [0] * n
    for i, p in enumerate(sa):
        rank[p] = i
    lcp = [0] * max(n - 1, 0)
    h = 0
    for i in range(n):
        if rank[i] == n - 1:
            h = 0
            continue
        j = sa[rank[i] + 1]
        while i + h < n and j + h < n and s[i + h] == s[j + h]:
            h += 1
        lcp[rank[i]] = h
        if h > 0:
            h -= 1
    return lcp
