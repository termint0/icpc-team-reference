class TwoSAT:
    """Variables 0..n-1. Literal for variable i: i*2 (true) / i*2+1 (false);
    use lit(i, val)."""

    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(2 * n)]

    @staticmethod
    def lit(i, val=True):
        return 2 * i + (0 if val else 1)

    def add_or(self, a, b):
        """Clause (a OR b) over literals."""
        self.adj[a ^ 1].append(b)
        self.adj[b ^ 1].append(a)

    def add_implies(self, a, b):
        self.add_or(a ^ 1, b)

    def solve(self):
        """Returns list of bools, or None if unsatisfiable."""
        comp, _, _ = scc(self.adj)
        res = []
        for i in range(self.n):
            if comp[2 * i] == comp[2 * i + 1]:
                return None
            res.append(comp[2 * i] < comp[2 * i + 1])
        return res
