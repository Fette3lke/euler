from euler import *
import math
from scipy.misc import factorial
import numpy as np


def contfrac(n0):
    cnt = 0
    a0 = np.floor(n0)
    n = n0
    an = []
    while cnt < 105:
        i = np.floor(n)
        a1 = (1./(n - i))
        an.append(i)
        n = a1
        cnt += 1
#        print type(a1), a1, i
    return an

def sqrcfrac(n):
    m = 0
    d = 1
    a0 = math.floor(math.sqrt(n))
    if a0**2 == n:
        return [n]
    a = a0
    
    an = [a0]

    cnt = 0
    while 1:
        m1 = d * a - m
        d1 = (n - m1**2) / d
        a1 = math.floor((a0+m1)/d1)
        if cnt == 0:
            start = [a1,m1,d1]
        
        a = a1
        m = m1
        d = d1
        
#        print a,m,d

        if cnt > 0 and [a,m,d] == start:
            return an
        an.append(int(a1))
        cnt += 1


primes = genprimes2(100000)

def factors(a):
    f = set([])
    for i in primes:
        if not a % i:
            f.add(i)

    return f
            

def kuerzen(a,b):    
    af = factors(a)
    bf = factors(b)
    gem = af.intersection(bf)
    while gem:
        for f in gem:
            a /= f
            b /= f

        af = factors(a)
        bf = factors(b)
        gem = af.intersection(bf)
    return int(a), int(b)
    
def approx(cf):
#    s = 0
    p = [cf[0], cf[0] * cf[1] + 1]
    q = [1, cf[1] ]
    l = len(cf)-1 
    if l % 2:
        end = 2 * l +1
    else:
        end = l
    for i in range(2, end):
        j = ((i-1) % l) + 1
        p.append( cf[j] * p[i-1] + p[i-2] )
        q.append( cf[j] * q[i-1] + q[i-2] )
        
    return [p[-1], q[-1]]


def pell(n, cf):
    i = 0
    h, k = approx(cf)
#        print h, k
    return h, k

#def perl(n0):
#    n0 = np.sqrt(n0)
#    cnt = 0
#    a0 = np.floor(n0)
#    n = n0
#    an = []
#    while cnt < 105:
#        i = np.floor(n)
#        a1 = np.longdouble(1./(n - i))
#        an.append(i)
#        n = a1
#        cnt += 1
#        print type(a1), a1, i
#    return an

def gpell(n):
    cf = sqrcfrac(n)
    return pell(n, cf)

ncheck = 10000
chk = [i for i in range(1,ncheck) if (np.sqrt(i)!=np.floor(np.sqrt(i)))]

maxx = 1
maxxi= 0
maxxy= 0

for i in chk:
    x, y =  gpell(i)
#    print i, " :: ",x, y
    if x > maxx:
        maxx = x
        maxxy= y
        maxxi= i        

        print maxxi, maxx, maxxy
