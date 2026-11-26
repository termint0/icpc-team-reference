def tree_diameter(adj):
    """adj[u] = [(v, w)] with w >= 0. Returns (length, path of vertices)."""
    def far(s):
        dist = {s: 0}
        par = {s: -1}
        st = [s]
        best = s
        while st:
            u = st.pop()
            if dist[u] > dist[best]:
                best = u
            for v, w in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + w
                    par[v] = u
                    st.append(v)
        return best, dist[best], par
    a, _, _ = far(0)
    b, d, par = far(a)
    path = []
    while b != -1:
        path.append(b)
        b = par[b]
    return d, path
