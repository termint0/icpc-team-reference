def rerooting(adj, e, merge, lift, finalize, root=0):
    """Compute for every v the DP value of the whole tree rooted at v.
    dp[v] = finalize(v, merge_{c child}(lift(dp[c], c, v))), with merge
    associative + commutative with identity e. Returns the list ans."""
    n = len(adj)
    par = [-1] * n
    order = [root]
    for u in order:
        for v in adj[u]:
            if v != par[u]:
                par[v] = u
                order.append(v)
    ch = [[v for v in adj[u] if v != par[u]] for u in range(n)]
    down = [None] * n
    for u in reversed(order):
        acc = e
        for c in ch[u]:
            acc = merge(acc, lift(down[c], c, u))
        down[u] = finalize(u, acc)
    upc = [e] * n  # contribution from the parent side, already lifted to v
    ans = [None] * n
    for u in order:
        cs = ch[u]
        k = len(cs)
        contrib = [lift(down[c], c, u) for c in cs]
        pref = [e] * (k + 1)
        for i in range(k):
            pref[i + 1] = merge(pref[i], contrib[i])
        suf = e
        for i in range(k - 1, -1, -1):
            ex = merge(merge(upc[u], pref[i]), suf)
            upc[cs[i]] = lift(finalize(u, ex), u, cs[i])
            suf = merge(contrib[i], suf)
        ans[u] = finalize(u, merge(upc[u], pref[k]))
    return ans
