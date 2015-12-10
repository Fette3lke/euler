#!/usr/bin/python
from euler import *
def circ(n):
    nums = []
    s = str(n)
    l = len(s)
    for i in range(l):
        temp = 0
        for j in range(l-1):
            temp += int(s[j+1]) * 10**(l-j-1)
        temp += int(s[0])
        nums.append(temp)
        s = str(temp)
    return nums

limit=10**6
primes = genprimes(limit)
print "numprimes:", len(primes)
#for p in primes:
#    if not isprime(p):
#        print p
#
#exit()
    

#print primes
#print len(primes)

cprimes = set([2, 5])

for p in primes:
    if p in cprimes or any(char in str(p) for char in ['0','2','4','6','8','5']):
#    if p in cprimes or '0' in str(p):
        continue
    c = circ(p)
    if sum(a in primes for a in c) == len(c):
        cprimes.update(c)
#        primes.difference_update(c)

print cprimes
#print circ(177773)
print len(cprimes)


#for i in cprimes:
#    if any(char in str(i) for char in ['0','2','4','6','8','5']):
#        print i

#print (4444) in primes
#print 4444 % 2
