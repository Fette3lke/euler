# http://mathworld.wolfram.com/PartitionFunctionP.html
#from euler import memoize
import numpy as np

LIMIT = 1000000
results = np.zeros(LIMIT, dtype=np.int32)
results[1] = 1
def memoize(func):
    #results = {}
    def helper(arg):
        if arg < 0:
             return 0
        if results[arg] == 0:
            results[arg] = func(arg)
        return results[arg]
    return helper


@memoize
def P(n):
    #print n
    if n < 0:
        return 0
    if n == 0:
        return 1
    return sum([(-1)**(k+1) *
        ((P(n - (k * (3*k-1))/2)) +
        (P(n - (k *(3*k+1))/2))) % LIMIT
        for k in range(1,n+1)]) % LIMIT

i = 0
while True:
    i += 1
    n = P(i)
    if (i % 1000) == 0:
        print i, n
    if (n % 1000000) == 0:
        print i, n
        break
