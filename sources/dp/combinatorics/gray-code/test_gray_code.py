from gray_code import gray, gray_inverse


def test_roundtrip():
    for n in range(1, 1000):
        assert gray_inverse(gray(n)) == n


def test_sequence_is_a_cyclic_gray_code():
    seq = [gray(i) for i in range(1 << 6)]
    assert sorted(seq) == list(range(64))
    assert all(bin(x ^ y).count("1") == 1 for x, y in zip(seq, seq[1:] + seq[:1]))
    assert gray(0) == 0 and gray(1) == 1 and gray(2) == 3 and gray(3) == 2
