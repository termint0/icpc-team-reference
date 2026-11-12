def scc(adj):
    n = len(adj); tin = [-1]*n; low = [0]*n; root = [-1]*n
    st = []; comps = []; t = 0
    for s in range(n):
        if tin[s] >= 0: continue
        tin[s] = low[s] = t; t += 1; st.append(s); call = [(s, 0)]
        while call:
            v, i = call.pop()
            if i < len(adj[v]):
                call.append((v, i+1)); u = adj[v][i]
                if tin[u] < 0:
                    tin[u] = low[u] = t; t += 1; st.append(u); call.append((u, 0))
                elif root[u] < 0:
                    low[v] = min(low[v], tin[u])
            else:
                if call: low[call[-1][0]] = min(low[call[-1][0]], low[v])
                if low[v] == tin[v]:
                    c = []
                    while not c or c[-1] != v:
                        c.append(st.pop()); root[c[-1]] = v
                    comps.append(c[::-1])
    cond = [[] for _ in adj]
    for v in range(n):
        for u in adj[v]:
            if root[v] != root[u]: cond[root[v]].append(root[u])
    return comps, cond, root
