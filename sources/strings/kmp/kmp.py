def prefix_function(s):
    """pi[i] = length of the longest proper border of s[:i+1]."""
    pi = [0] * len(s)
    for i in range(1, len(s)):
        k = pi[i - 1]
        while k and s[i] != s[k]: k = pi[k - 1]
        if s[i] == s[k]: k += 1
        pi[i] = k
    return pi
def kmp_search(text, pat):
    """Start indices of all (overlapping) occurrences of pat in text."""
    if not pat: return list(range(len(text) + 1))
    pi = prefix_function(pat)
    res, k = [], 0
    for i, c in enumerate(text):
        while k and (k == len(pat) or c != pat[k]):
            k = pi[k - 1]
        if c == pat[k]: k += 1
        if k == len(pat): res.append(i - k + 1)
    return res
