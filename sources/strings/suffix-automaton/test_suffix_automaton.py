from suffix_automaton import SuffixAutomaton
import random


def rs(n, alpha="ab"):
    return "".join(random.choice(alpha) for _ in range(n))


def test_suffix_automaton():
    for _ in range(300):
        s = rs(random.randrange(0, 15), "abc")
        sam = SuffixAutomaton(s)
        subs = {s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)}
        assert sam.count_distinct() == len(subs)
        for _ in range(10):
            t = rs(random.randrange(0, 6), "abc")
            assert sam.contains(t) == (t == "" or t in subs)
        t = rs(random.randrange(0, 15), "abc")
        best = max((j - i for i in range(len(t)) for j in range(i + 1, len(t) + 1) if t[i:j] in subs), default=0)
        ln, end = sam.longest_common_substring(t)
        assert ln == best
        if ln:
            assert t[end - ln:end] in subs
