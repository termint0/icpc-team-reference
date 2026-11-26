from math import gcd
def count_divisible_by_any(N, nums):
    """#{x in [1, N] : x divisible by at least one of nums}, by
    inclusion-exclusion over lcm's with pruning."""
    nums = sorted(set(nums))
    if 1 in nums:
        return N
    res = 0

    def rec(i, l, sign, k):
        nonlocal res
        for j in range(i, len(nums)):
            nl = l // gcd(l, nums[j]) * nums[j]
            if nl > N:
                continue
            res += sign * (N // nl)
            rec(j + 1, nl, -sign, k + 1)
    rec(0, 1, 1, 0)
    return res

def count_coprime(N, n):
    """#{x in [1, N] : gcd(x, n) = 1}."""
    primes, m, p = [], n, 2
    while p * p <= m:
        if m % p == 0:
            primes.append(p)
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        primes.append(m)
    return N - count_divisible_by_any(N, primes)
