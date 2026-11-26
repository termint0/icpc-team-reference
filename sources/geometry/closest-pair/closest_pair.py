def dist2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def closest_pair(pts):
    """Returns (squared distance, p, q) of the closest pair. O(n log n),
    needs at least 2 points (duplicates allowed)."""
    P = sorted(pts)
    best = [float("inf"), None, None]
    def upd(p, q):
        d = dist2(p, q)
        if d < best[0]:
            best[0], best[1], best[2] = d, p, q
    def rec(l, r):
        if r - l <= 3:
            sub_ = sorted(P[l:r], key=lambda p: p[1])
            for i in range(len(sub_)):
                for j in range(i + 1, len(sub_)):
                    upd(sub_[i], sub_[j])
            return sub_
        m = (l + r) // 2
        midx = P[m][0]
        merged = sorted(rec(l, m) + rec(m, r), key=lambda p: p[1])
        strip = [p for p in merged if (p[0] - midx) ** 2 < best[0]]
        for i, p in enumerate(strip):
            for q in strip[i + 1:]:
                if (q[1] - p[1]) ** 2 >= best[0]:
                    break
                upd(p, q)
        return merged
    rec(0, len(P))
    return tuple(best)
