def sliding_window_min(a, k):
    """min of every window of length k (use negated values for max)."""
    from collections import deque
    dq, out = deque(), []
    for i, x in enumerate(a):
        while dq and a[dq[-1]] >= x: dq.pop()
        dq.append(i)
        if dq[0] <= i - k: dq.popleft()
        if i >= k - 1: out.append(a[dq[0]])
    return out
