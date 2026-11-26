def gray(n):
    return n ^ (n >> 1)

def gray_inverse(g):
    n = 0
    while g:
        n ^= g
        g >>= 1
    return n
