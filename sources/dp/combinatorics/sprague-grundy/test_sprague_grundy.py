from sprague_grundy import grundy_table, mex


def test_grundy():
    g = grundy_table(30, lambda n, g: [g[k] for k in range(n)])
    assert g == list(range(31))   # Nim heap
    g = grundy_table(30, lambda n, g: [g[n - k] for k in (1, 2) if n >= k])
    assert g == [n % 3 for n in range(31)]
    kayles = grundy_table(11, lambda n, g: [g[a] ^ g[n - 1 - a] for a in range(n)] +
                          [g[a] ^ g[n - 2 - a] for a in range(n - 1) if n >= 2])
    assert kayles == [0, 1, 2, 3, 1, 4, 3, 2, 1, 4, 2, 6]
    assert mex([0, 1, 3]) == 2 and mex([]) == 0
