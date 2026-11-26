from collections import defaultdict
def digit_dp(N, init, step, accept, base=10):
    """Count x in [0, N] (no leading zeros; 0 is the empty digit string) with
    accept(final_state). State starts at init and is updated by
    step(state, digit) -> new state, or None to reject. O(len * states * base)."""
    digs = []
    x = N
    while x:
        digs.append(x % base)
        x //= base
    digs.reverse()
    # key: (tight, started, state)
    cur = {(True, False, init): 1}
    for d in digs:
        nxt = defaultdict(int)
        for (tight, started, st), c in cur.items():
            for dig in range(d + 1 if tight else base):
                nt = tight and dig == d
                if not started and dig == 0:
                    nxt[(nt, False, st)] += c
                else:
                    ns = step(st, dig)
                    if ns is not None:
                        nxt[(nt, True, ns)] += c
        cur = nxt
    return sum(c for (_, _, st), c in cur.items() if accept(st))
