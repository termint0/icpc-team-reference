class Sparse:
    def __init__(self, a):
        self.t = [list(a)]
        j = 1
        while 2**j <= len(a):
            prev = self.t[-1]
            half = 2 ** (j - 1)
            self.t.append([prev[i] <op> prev[i + half] 
                for i in range(len(a) - 2**j + 1)])
            j += 1

    def query(self, l, r):  # a[l] <op> ... <op> a[r-1], requires l < r
        j = (r - l).bit_length() - 1
        return self.t[j][l] < op > self.t[j][r - 2**j]
