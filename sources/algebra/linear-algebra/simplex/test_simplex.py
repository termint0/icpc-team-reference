from fractions import Fraction
from simplex import Simplex
import itertools
import random


def vertex_enum_lp(A, b, c):
    n = len(c)
    rows = [(list(map(Fraction, r)), Fraction(bb)) for r, bb in zip(A, b)]
    for j in range(n):
        rows.append(([Fraction(-1 if k == j else 0) for k in range(n)], Fraction(0)))
    best = None
    for comb in itertools.combinations(range(len(rows)), n):
        M = [rows[i][0][:] + [rows[i][1]] for i in comb]
        # gaussian elimination
        ok = True
        for col in range(n):
            piv = next((r for r in range(col, n) if M[r][col] != 0), None)
            if piv is None:
                ok = False
                break
            M[col], M[piv] = M[piv], M[col]
            M[col] = [x / M[col][col] for x in M[col]]
            for r in range(n):
                if r != col and M[r][col] != 0:
                    M[r] = [x - M[r][col] * y for x, y in zip(M[r], M[col])]
        if not ok:
            continue
        x = [M[i][n] for i in range(n)]
        if all(sum(a * xi for a, xi in zip(r, x)) <= bb for r, bb in rows):
            v = sum(Fraction(ci) * xi for ci, xi in zip(c, x))
            if best is None or v > best:
                best = v
    return best


def test_simplex():
    for _ in range(300):
        n, m = random.randrange(1, 4), random.randrange(1, 5)
        A = [[random.randint(-3, 3) for _ in range(n)] for _ in range(m)]
        b = [random.randint(-4, 10) for _ in range(m)]
        for j in range(n):   # box constraints keep it bounded
            A.append([1 if k == j else 0 for k in range(n)])
            b.append(8)
        c = [random.randint(-4, 5) for _ in range(n)]
        st, val, x = Simplex(A, b, c).solve()
        exp = vertex_enum_lp(A, b, c)
        if exp is None:
            assert st == "infeasible"
        else:
            assert st == "optimal" and abs(val - float(exp)) < 1e-6, (A, b, c, val, exp)
            assert all(xi >= -1e-7 for xi in x)
            assert all(sum(a * xi for a, xi in zip(r, x)) <= bb + 1e-6 for r, bb in zip(A, b))
            assert abs(sum(ci * xi for ci, xi in zip(c, x)) - val) < 1e-6
    assert Simplex([[1, -1]], [1], [1, 1]).solve()[0] == "unbounded"
    assert Simplex([[1], [-1]], [1, -2], [1]).solve()[0] == "infeasible"
    st, v, x = Simplex([[1, 1], [1, 3]], [4, 6], [3, 2]).solve()
    assert st == "optimal" and abs(v - 12) < 1e-9
