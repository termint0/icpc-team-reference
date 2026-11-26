def min_rotation(s):
    """Start index of the lexicographically smallest rotation."""
    n = len(s)
    s2 = s + s
    i = ans = 0
    while i < n:
        ans = i
        j, k = i + 1, i
        while j < 2 * n and s2[k] <= s2[j]:
            k = i if s2[k] < s2[j] else k + 1
            j += 1
        while i <= k:
            i += j - k
    return ans
