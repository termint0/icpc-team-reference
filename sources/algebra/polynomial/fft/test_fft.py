from fft import convolution_fft
import random


def test_convolutions():
    for _ in range(100):
        a = [random.randrange(0, 10 ** 9) for _ in range(random.randrange(1, 40))]
        b = [random.randrange(0, 10 ** 9) for _ in range(random.randrange(1, 40))]
        exp = [0] * (len(a) + len(b) - 1)
    for _ in range(100):
        a = [random.randrange(-100, 100) for _ in range(random.randrange(1, 40))]
        b = [random.randrange(-100, 100) for _ in range(random.randrange(1, 40))]
        exp = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                exp[i + j] += x * y
        assert convolution_fft(a, b) == exp
