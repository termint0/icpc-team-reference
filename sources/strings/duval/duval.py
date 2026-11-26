def duval(s):
    """Lyndon factorisation: list of (start, end) of non-increasing Lyndon
    words whose concatenation is s."""
    n, i, res = len(s), 0, []
    while i < n:
        j, k = i + 1, i
        while j < n and s[k] <= s[j]:
            k = i if s[k] < s[j] else k + 1
            j += 1
        while i <= k:
            res.append((i, i + j - k))
            i += j - k
    return res
