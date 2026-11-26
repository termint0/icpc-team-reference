class SuffixAutomaton:
    """Minimal DFA of all suffixes; O(n) states. Supports distinct substring
    count, substring test and longest common substring."""
    def __init__(self, s=""):
        self.next = [{}]
        self.link = [-1]
        self.len = [0]
        self.last = 0
        for c in s: self.extend(c)

    def extend(self, c):
        cur = len(self.len)
        self.len.append(self.len[self.last] + 1)
        self.next.append({})
        self.link.append(0)
        p = self.last
        while p != -1 and c not in self.next[p]:
            self.next[p][c] = cur
            p = self.link[p]
        if p != -1:
            q = self.next[p][c]
            if self.len[p] + 1 == self.len[q]: self.link[cur] = q
            else:
                cl = len(self.len)
                self.len.append(self.len[p] + 1)
                self.next.append(dict(self.next[q]))
                self.link.append(self.link[q])
                while p != -1 and self.next[p].get(c) == q:
                    self.next[p][c] = cl
                    p = self.link[p]
                self.link[q] = self.link[cur] = cl
        self.last = cur

    def count_distinct(self):
        """Number of distinct non-empty substrings."""
        return sum(self.len[v] - self.len[self.link[v]] for v in range(1, len(self.len)))

    def contains(self, t):
        v = 0
        for c in t:
            v = self.next[v].get(c)
            if v is None: return False
        return True

    def longest_common_substring(self, t):
        """Length and end index (in t, exclusive) of the longest substring
        of t that occurs in the automaton's string."""
        v = l = 0
        best, best_end = 0, 0
        for i, c in enumerate(t):
            while v and c not in self.next[v]:
                v = self.link[v]
                l = self.len[v]
            if c in self.next[v]:
                v = self.next[v][c]
                l += 1
            if l > best: best, best_end = l, i + 1
        return best, best_end
