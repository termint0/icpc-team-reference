from digit_dp import digit_dp
import random


def test_digit_dp():
    for _ in range(100):
        N = random.randrange(0, 3000)
        s = random.randrange(0, 20)
        got = digit_dp(N, 0, lambda st, d: st + d if st + d <= s else None, lambda st: st == s)
        assert got == sum(1 for x in range(N + 1) if sum(map(int, str(x))) == s)
        # no two adjacent equal digits (state = last digit, -1 for none)
        got = digit_dp(N, -1, lambda st, d: None if st == d else d, lambda st: True)
        assert got == sum(1 for x in range(N + 1) if all(p != q for p, q in zip(str(x), str(x)[1:])))
    assert digit_dp(10**18, 0, lambda st, d: st + d, lambda st: st == 1) == 19  # 1, 10, ..., 10^18
    assert digit_dp(255, 0, lambda st, d: st + d, lambda st: st % 2 == 0, base=2) == 128
