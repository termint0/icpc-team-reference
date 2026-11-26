from trie import Trie


def test_tries():
    words = ['', 'a', 'ab', 'abc', 'abd', 'b', 'ab', 'bcd']
    t = Trie()
    for w in words:
        t.insert(w)
    assert t.count('ab') == 2 and t.count('abc') == 1 and (t.count('x') == 0)
    assert t.count_prefix('ab') == 4 and t.count_prefix('b') == 2 and (t.count_prefix('') == len(words))
    assert t.erase('ab') and t.count('ab') == 1 and (not t.erase('zzz'))
    assert t.count_prefix('ab') == 3 and t.count_prefix('') == len(words) - 1
