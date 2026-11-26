from primitives import cross, cross2, dist2, dot, on_segment, sgn, sub


def test_primitives():
    assert sub((5, 7), (2, 3)) == (3, 4)
    assert dot((1, 2), (3, 4)) == 11
    assert cross2((1, 0), (0, 1)) == 1 and cross2((0, 1), (1, 0)) == -1
    assert cross((0, 0), (1, 0), (1, 1)) > 0      # left turn
    assert cross((0, 0), (1, 0), (1, -1)) < 0     # right turn
    assert cross((0, 0), (1, 1), (2, 2)) == 0     # collinear
    assert dist2((0, 0), (3, 4)) == 25
    assert [sgn(-5), sgn(0), sgn(2.5)] == [-1, 0, 1]
    assert on_segment((0, 0), (4, 4), (2, 2)) and on_segment((0, 0), (4, 4), (4, 4))
    assert not on_segment((0, 0), (4, 4), (5, 5)) and not on_segment((0, 0), (4, 4), (2, 3))
