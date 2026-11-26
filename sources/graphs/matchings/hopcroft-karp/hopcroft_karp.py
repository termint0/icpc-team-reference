def hopcroft_karp(nl, nr, adj):
    """Max bipartite matching, O(E sqrt V). adj[u] = right nodes of left u.
    Returns (size, matchL, matchR)."""
    BIG = 1 << 30
    mL, mR = [-1] * nl, [-1] * nr
    res = 0
    while True:
        dist = [BIG] * nl
        q = [u for u in range(nl) if mL[u] == -1]
        for u in q:
            dist[u] = 0
        found = False
        for u in q:
            for v in adj[u]:
                w = mR[v]
                if w == -1:
                    found = True
                elif dist[w] == BIG:
                    dist[w] = dist[u] + 1
                    q.append(w)
        if not found:
            return res, mL, mR
        it = [0] * nl
        for s in range(nl):
            if mL[s] != -1:
                continue
            stack = [s]
            while stack:
                u = stack[-1]
                if it[u] < len(adj[u]):
                    v = adj[u][it[u]]
                    it[u] += 1
                    w = mR[v]
                    if w == -1:
                        for x in stack:
                            vx = adj[x][it[x] - 1]
                            mL[x] = vx
                            mR[vx] = x
                        res += 1
                        break
                    if dist[w] == dist[u] + 1:
                        stack.append(w)
                else:
                    dist[u] = BIG
                    stack.pop()
