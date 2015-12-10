from euler import *
import numpy as np

primes = genprimes2(1000)

def factors(a):
    f = set([])
    for i in primes:
        if not a % i:
            f.add(i)
        if (i > np.sqrt(a)+1):
            break
    return f


def totient(n):
    fac = factors(n)
    p = 1
    for f in fac:
        p *= (1.-1./f)

    return (n * p)

maxv = 0
maxi = 0
for i in range(1,10):
    ntot = float(i) / totient(i)

    if ntot > maxv:
        print i, ntot
        maxv = ntot
        maxi = i

print maxi, maxv
