def kuhn(adj, m):
    mt = [-1] * m  # mt[r] = left vertex matched to right vertex r
    def try_(v):
        for u in adj[v]:
            if not seen[u]:
                seen[u] = 1
                if mt[u] < 0 or try_(mt[u]):  # u free, or its partner can move elsewhere
                    mt[u] = v; return True
        return False
    for v in range(len(adj)):
        seen = [0] * m
        try_(v)
    return mt
