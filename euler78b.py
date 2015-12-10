# http://mathworld.wolfram.com/PartitionFunctionP.html
from euler import memoize

@memoize
def P(n):
    #print n
    if n < 0:
        return 0
    if n == 0:
        return 1
    return sum([(-1)**(k+1) *
        ((P(n - (k * (3*k-1))/2)) +
        (P(n - (k *(3*k+1))/2)))
        for k in range(1,n+1)])

i = 0
while True:
    i += 1
    n = P(i)
    if (i % 1000) == 0:
        print i, n
    if (n % 1000000) == 0:
        print i, n
        break
