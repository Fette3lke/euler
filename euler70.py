from euler import *
import numpy as np
from itertools import permutations
from collections import defaultdict

#primes = genprimes2(3163)
primes = genprimes2(31630)

#def factors(a):
#    b = a
#    if a in primes:
#        return set([a])
#    f = set([])
#    for i in primes:
#        if not a % i:
#            f.add(i)
#            b = b / i
#        if (i > np.sqrt(a)+1):
#            break
#    if b != 1:
#        f.add(b)
#    if len(f) == 0:
#        return set([a])
#    return f

def isPerm(a,b):
    if getHash(a) == getHash(b):
        return True
    return False

def getHash(a):
    return "".join(sorted(str(int(a))))

hashtab = defaultdict(list)

def totient(n):
    fac = factors(n)
    p = 1
    for f in fac:
        p *= (1.-1./f)

    return np.round(n * p)

#totprimes = [ for i in primes ]

minv = np.inf
mini = 0

#tot = [totient(i) for i in range(1,10000)]

cnt = 0
for p in permutations(primes, 2):
    n = p[0] * p[1]
    if n > 1e7:
        continue
#    tn = totient(n)
    tn = (p[0]-1) * (p[1] -1)
    if isPerm(n, tn):
        print n, tn
        q = (1. * n) / tn
        if minv > q :
            minv = q
            mini = n
    cnt += 1
#    if not cnt % 1000:
#        print cnt, p[0], p[1], n, tn

print mini, minv
