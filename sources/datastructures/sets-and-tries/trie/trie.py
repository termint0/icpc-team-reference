class Trie:
    """Trie over strings (or any sequences of hashables)."""
    def __init__(self):
        self.nxt = [{}]
        self.cnt = [0]      # words passing through the node
        self.end = [0]      # words ending at the node

    def insert(self, s):
        v = 0
        self.cnt[0] += 1
        for c in s:
            if c not in self.nxt[v]:
                self.nxt[v][c] = len(self.nxt)
                self.nxt.append({})
                self.cnt.append(0)
                self.end.append(0)
            v = self.nxt[v][c]
            self.cnt[v] += 1
        self.end[v] += 1

    def _walk(self, s):
        v = 0
        for c in s:
            v = self.nxt[v].get(c)
            if v is None: return None
        return v

    def count(self, s):
        v = self._walk(s)
        return 0 if v is None else self.end[v]

    def count_prefix(self, p):
        v = self._walk(p)
        return 0 if v is None else self.cnt[v]

    def erase(self, s):
        if not self.count(s): return False
        v = 0
        self.cnt[0] -= 1
        for c in s:
            v = self.nxt[v][c]
            self.cnt[v] -= 1
        self.end[v] -= 1
        return True
