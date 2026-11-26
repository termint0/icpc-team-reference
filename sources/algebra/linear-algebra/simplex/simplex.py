class Simplex:
    """maximize c.x subject to A x <= b, x >= 0. Dense tableau (KACTL port).
    solve() returns (status, value, x): status 'optimal', 'infeasible' or
    'unbounded'."""
    EPS = 1e-9

    def __init__(self, A, b, c):
        self.m, self.n = len(b), len(c)
        m, n = self.m, self.n
        self.N = [0] * (n + 1)
        self.B = [0] * m
        self.D = [[0.0] * (n + 2) for _ in range(m + 2)]
        for i in range(m):
            for j in range(n):
                self.D[i][j] = A[i][j]
        for i in range(m):
            self.B[i] = n + i
            self.D[i][n] = -1
            self.D[i][n + 1] = b[i]
        for j in range(n):
            self.N[j] = j
            self.D[m][j] = -c[j]
        self.N[n] = -1
        self.D[m + 1][n] = 1

    def _pivot(self, r, s):
        D, m, n = self.D, self.m, self.n
        a = D[r]
        inv = 1.0 / a[s]
        for i in range(m + 2):
            if i != r and abs(D[i][s]) > self.EPS:
                bb = D[i]
                inv2 = bb[s] * inv
                for j in range(n + 2):
                    bb[j] -= a[j] * inv2
                bb[s] = a[s] * inv2
        for j in range(n + 2):
            if j != s:
                D[r][j] *= inv
        for i in range(m + 2):
            if i != r:
                D[i][s] *= -inv
        D[r][s] = inv
        self.B[r], self.N[s] = self.N[s], self.B[r]

    def _simplex(self, phase):
        D, m, n, B, N = self.D, self.m, self.n, self.B, self.N
        x = m + phase - 1
        while True:
            s = -1
            for j in range(n + 1):
                if N[j] != -phase and (s == -1 or (D[x][j], N[j]) < (D[x][s], N[s])):
                    s = j
            if D[x][s] >= -self.EPS:
                return True
            r = -1
            for i in range(m):
                if D[i][s] <= self.EPS:
                    continue
                if r == -1 or (D[i][n + 1] / D[i][s], B[i]) < (D[r][n + 1] / D[r][s], B[r]):
                    r = i
            if r == -1:
                return False
            self._pivot(r, s)

    def solve(self):
        D, m, n, B = self.D, self.m, self.n, self.B
        r = 0
        for i in range(1, m):
            if D[i][n + 1] < D[r][n + 1]:
                r = i
        if m and D[r][n + 1] < -self.EPS:
            self._pivot(r, n)
            if not self._simplex(2) or D[m + 1][n + 1] < -self.EPS:
                return "infeasible", None, None
            for i in range(m):
                if B[i] == -1:
                    s = 0
                    for j in range(1, n + 1):
                        if (D[i][j], self.N[j]) < (D[i][s], self.N[s]):
                            s = j
                    self._pivot(i, s)
        ok = self._simplex(1)
        x = [0.0] * n
        for i in range(m):
            if B[i] < n:
                x[B[i]] = D[i][n + 1]
        if not ok:
            return "unbounded", None, None
        return "optimal", D[m][n + 1], x
