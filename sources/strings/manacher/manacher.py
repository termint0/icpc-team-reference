def manacher(s):
    """Returns (d1, d2): d1[i] = number of odd-length palindromes centred at
    i; d2[i] = number of even-length palindromes centred between i-1 and i.
    Longest odd palindrome around i has length 2*d1[i]-1, even 2*d2[i]."""
    n = len(s)
    d1 = [0] * n
    l, r = 0, -1
    for i in range(n):
        k = 1 if i > r else min(d1[l + r - i], r - i + 1)
        while i - k >= 0 and i + k < n and s[i - k] == s[i + k]: k += 1
        d1[i] = k
        if i + k - 1 > r: l, r = i - k + 1, i + k - 1
    d2 = [0] * n
    l, r = 0, -1
    for i in range(n):
        k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)
        while i - k - 1 >= 0 and i + k < n and s[i - k - 1] == s[i + k]:
            k += 1
        d2[i] = k
        if i + k - 1 > r: l, r = i - k, i + k - 1
    return d1, d2
def longest_palindrome(s):
    """(start, length) of the longest palindromic substring."""
    d1, d2 = manacher(s)
    best = (0, 0 if not s else 1)
    for i in range(len(s)):
        if 2 * d1[i] - 1 > best[1]:
            best = (i - d1[i] + 1, 2 * d1[i] - 1)
        if 2 * d2[i] > best[1]:
            best = (i - d2[i], 2 * d2[i])
    return best
