from euler import *

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
    if 2*m > num:
        return 1     # no more possible solutions
    ret = 1
    for p in range(1, num/2+1):
        if p < m:
            continue
        left = num - p
        if left >= p:
            ret += nsum(p, left)    # summands need to be increasing, to prevent duplicates
    return ret

i = 0
while True:
    i += 1
    n = nsum(1, i)
    if (i % 100) == 0:
        print i, n
    if (n % 1000000) == 0:
        print i, n
        break
