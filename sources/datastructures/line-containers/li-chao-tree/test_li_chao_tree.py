from li_chao_tree import LiChao
import random


def test_li_chao_and_cht():
    for _ in range(50):
        lines = [(random.randrange(-20, 21), random.randrange(-100, 101)) for _ in range(random.randrange(1, 30))]
        lc = LiChao(-50, 50)
        for i, (k, m) in enumerate(lines):
            lc.add_line(k, m)
            for x in (-50, -3, 0, 7, 50, random.randrange(-50, 51)):
                assert lc.query(x) == min((kk * x + mm for kk, mm in lines[:i + 1]))
    assert LiChao(0, 10).query(3) == float('inf')
