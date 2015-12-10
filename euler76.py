from euler import *


limit = 15
primes = genprimes2(limit)
primetable = set(primes)
ns = [0 for i in range(limit)]

for i in range(2, limit):
    for p in primes:
        if p > i:
            break
        if p > i/2.:
            break
        
        if (i - p) in primetable:
            ns[i] += 1        
    ns[i] += ns[i - 2]

