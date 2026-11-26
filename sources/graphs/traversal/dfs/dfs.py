def dfs_order(adj, s):
    """Iterative DFS. Returns (preorder, postorder, parent)."""
    n = len(adj)
    parent = [-2] * n
    parent[s] = -1
    pre, post, it, st = [s], [], [0] * n, [s]
    while st:
        u = st[-1]
        if it[u] < len(adj[u]):
            v = adj[u][it[u]]
            it[u] += 1
            if parent[v] == -2:
                parent[v] = u
                pre.append(v)
                st.append(v)
        else: post.append(st.pop())
    return pre, post, parent
