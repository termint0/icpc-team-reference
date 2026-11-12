def hungarian(a):
    n, m = len(a), len(a[0])            # needs n <= m
    u = [0]*(n+1); v = [0]*(m+1); p = [0]*(m+1); way = [0]*(m+1)
    for i in range(1, n+1):
        p[0] = i; j0 = 0
        minv = [float('inf')]*(m+1); used = [False]*(m+1)
        while True:
            used[j0] = True; i0 = p[j0]; delta = float('inf')
            for j in range(1, m+1):
                if not used[j]:
                    cur = a[i0-1][j-1] - u[i0] - v[j]
                    if cur < minv[j]: minv[j] = cur; way[j] = j0
                    if minv[j] < delta: delta = minv[j]; j1 = j
            for j in range(m+1):
                if used[j]: u[p[j]] += delta; v[j] -= delta
                else: minv[j] -= delta
            j0 = j1
            if p[j0] == 0: break
        while j0:
            j1 = way[j0]; p[j0] = p[j1]; j0 = j1
    ans = [0]*n                          # ans[i] = column assigned to row i
    for j in range(1, m+1):
        if p[j]: ans[p[j]-1] = j-1
    return -v[0], ans
