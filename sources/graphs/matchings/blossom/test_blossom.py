from blossom import blossom
import random


def max_matching_brute(n, edges):
    best = 0

    def rec(i, used, cnt):
        nonlocal best
        best = max(best, cnt)
        for j in range(i, len(edges)):
            u, v = edges[j]
            if u != v and not used >> u & 1 and not used >> v & 1:
                rec(j + 1, used | 1 << u | 1 << v, cnt + 1)
    rec(0, 0, 0)
    return best


def test_blossom():
    for _ in range(400):
        n = random.randrange(1, 10)
        edges = [(random.randrange(n), random.randrange(n)) for _ in range(random.randrange(0, 16))]
        adj = [[] for _ in range(n)]
        for u, v in edges:
            if u != v:
                adj[u].append(v)
                adj[v].append(u)
        size, match = blossom(n, adj)
        assert size == max_matching_brute(n, edges)
        for v in range(n):
            if match[v] != -1:
                assert match[match[v]] == v and match[v] in adj[v]
    # odd cycles (blossoms) explicitly
    n = 7
    adj = [[(i + 1) % n, (i - 1) % n] for i in range(n)]
    assert blossom(n, adj)[0] == 3
