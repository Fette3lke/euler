from euler import *

prime_ceil = 10000
primes = genprimes2(prime_ceil)

results = {}

def memoize(func):
    # results = {}
    def helper(*args):
        if args not in results:
            results[args] = func(*args)
        return results[args]
    return helper

@memoize
def nsum(m, num):
    # return number of prime sums of num, where all summands are >= m
    global prime_ceil
    global primes
    if m > num/2:
        return 0     # no more possible solutions
    if num > prime_ceil:
        prime_ceil *= 2     # increase number of primes if neccessary
        primes = genprimes2(prime_ceil)

    ret = 0
    for p in primes:
        if p < m:
            continue
        if p > num/2:
            break
        left = num - p
        if left in primes:
            ret += 1        # found a possible sum
        if left >= p:
            ret += nsum(p, left)    # summands need to be increasing, to prevent duplicates
    return ret

n = 2
i = 0
while n < 5000:
    i += 1
    n = nsum(2, i)
    if (i % 100) == 0:
        print i, n

print i, n
