def euler_tour(adj, root=0):
    """Returns (tin, tout, order): subtree of v is order[tin[v]:tout[v]];
    u is an ancestor of v iff tin[u] <= tin[v] < tout[u]."""
    n = len(adj)
    tin, tout, order = [0] * n, [0] * n, []
    par = [-1] * n
    it = [0] * n
    st = [root]
    tin[root] = 0
    order.append(root)
    while st:
        u = st[-1]
        if it[u] < len(adj[u]):
            v = adj[u][it[u]]
            it[u] += 1
            if v != par[u]:
                par[v] = u
                tin[v] = len(order)
                order.append(v)
                st.append(v)
        else:
            tout[u] = len(order)
            st.pop()
    return tin, tout, order
