def mo_algorithm(n, queries, add, remove, get):
    """queries: list of (l, r) half-open. add(i)/remove(i) update the current
    window; get() returns its answer. Returns answers in input order."""
    q = len(queries)
    block = max(1, int(n / max(1, q) ** 0.5))
    order = sorted(range(q), key=lambda i: (queries[i][0] // block,
                                            queries[i][1] if (queries[i][0] // block) % 2 == 0 else -queries[i][1]))
    ans = [None] * q
    cl = cr = 0
    for qi in order:
        l, r = queries[qi]
        while cl > l:
            cl -= 1
            add(cl)
        while cr < r:
            add(cr)
            cr += 1
        while cl < l:
            remove(cl)
            cl += 1
        while cr > r:
            cr -= 1
            remove(cr)
        ans[qi] = get()
    return ans
