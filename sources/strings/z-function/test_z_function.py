from z_function import z_function
import random
def rs(n, alpha="ab"):
    return "".join(random.choice(alpha) for _ in range(n))

def test_prefix_kmp_z():
    for _ in range(500):
        s = rs(random.randrange(0, 20))
        z = z_function(s)
        for i in range(len(s)):
            assert z[i] == (len(s) if i == 0 else next((k for k in range(len(s) - i + 1) if k == len(s) - i or s[k] != s[i + k])))
