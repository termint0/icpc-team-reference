def next_greater(a):
    """idx of next strictly greater element to the right, or len(a)."""
    res, st = [len(a)] * len(a), []
    for i, x in enumerate(a):
        while st and a[st[-1]] < x: res[st.pop()] = i
        st.append(i)
    return res

def prev_smaller(a):
    """idx of previous strictly smaller element to the left, or -1."""
    res, st = [-1] * len(a), []
    for i, x in enumerate(a):
        while st and a[st[-1]] >= x: st.pop()
        res[i] = st[-1] if st else -1
        st.append(i)
    return res

def largest_rectangle(h):
    """Largest rectangle area in a histogram (monotone stack)."""
    st, best = [], 0
    for i, x in enumerate(list(h) + [0]):
        while st and h[st[-1]] >= x:
            height = h[st.pop()]
            left = st[-1] if st else -1
            best = max(best, height * (i - left - 1))
        st.append(i)
    return best
