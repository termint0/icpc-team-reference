from convex_hull_trick import MonotoneCHT
import random


def test_li_chao_and_cht():
    for _ in range(50):
        lines = [(random.randrange(-20, 21), random.randrange(-100, 101)) for _ in range(random.randrange(1, 30))]
        cht = MonotoneCHT()
        for i, (k, m) in enumerate(sorted(lines, key=lambda z: -z[0])):
            cht.add(k, m)
        for x in range(-60, 61):
            assert cht.query(x) == min((k * x + m for k, m in lines))
