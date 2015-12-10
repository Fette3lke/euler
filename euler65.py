from euler import *
import math
from scipy.misc import factorial
import numpy as np

e = np.float128(2.7182818284590452353602874713527)

def contfrac(n0):
    n0 = np.float128(n0)
    cnt = 0
    a0 = np.floor(n0)
    n = n0
    an = []
    while cnt < 105:
        i = np.floor(n)
        a1 = np.longdouble(1./(n - i))
        an.append(i)
        n = a1
        cnt += 1
#        print type(a1), a1, i
    return an

def contfrac2(num, den):
#    n0 = num // den
    cnt = 0
#    a0 = num // den
#    n = n0
    an = []
    while cnt < 105:
        i = num // den
        num = num % den
        tmp = num
        num = den
        den = tmp
        num, den = kuerzen(num, den)
#        a1 = np.longdouble(1./(n - i))
        an.append(i)
 #       n = a1
        cnt += 1
#        print cnt, i
#        print type(a1), a1, i
    return an

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
    
def calcE(n):
    num = 0
    den = 1
    for i in range(n):
        n = 2*i + 2
        d = factorial(2*i+1, True)
        n, d = kuerzen(n, d)
        num = (num * d) + n * den
        den = den * d
        num, den = kuerzen(num, den)
    return num, den

def approx(cf, n):
    num = 0
    den = 1
#    s = 0
    for i in range(n, -1, -1):
        num += int(cf[i])*den
        tmp = num
        num = den
        den = tmp
        num, den = kuerzen(num,den)
#        s += cf[i]
#        s = 1./s
#    num += cf[0] * den
    return [num, den]

def ssum(i):
    return sum([int(j) for j in str(i)])

def seqa(n):
    if (n % 3) == 1: return 2*(n/3 + 1)
    return 1

cf0 = [2]
for i in range(100):
    cf0.append(seqa(i))
    
#cnt = 0
#for i in range(2, 10001):
#    cf = contfrac(i)
#    l = len(cf) - 1 
#    if l % 2:
#        cnt += 1
#        print cf, l
#
#print cnt
