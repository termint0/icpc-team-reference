from manacher import longest_palindrome, manacher
import random


def rs(n, alpha="ab"):
    return "".join(random.choice(alpha) for _ in range(n))


def test_manacher():
    for _ in range(500):
        s = rs(random.randrange(0, 20))
        d1, d2 = manacher(s)
        for i in range(len(s)):
            odd = sum(1 for k in range(0, i + 1) if i + k < len(s) and s[i - k:i + k + 1] == s[i - k:i + k + 1][::-1]
                      and all(s[i - j:i + j + 1] == s[i - j:i + j + 1][::-1] for j in range(k + 1)))
            assert d1[i] == odd
            ev = 0
            while i - ev - 1 >= 0 and i + ev < len(s) and s[i - ev - 1:i + ev + 1] == s[i - ev - 1:i + ev + 1][::-1]:
                ev += 1
            assert d2[i] == ev
        st, ln = longest_palindrome(s)
        brute = max((j - i for i in range(len(s)) for j in range(i + 1, len(s) + 1) if s[i:j] == s[i:j][::-1]), default=0)
        assert ln == brute and s[st:st + ln] == s[st:st + ln][::-1]
    assert longest_palindrome("") == (0, 0)
