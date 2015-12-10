import math
import numpy as np

def memoize(func):
    results = {}
    def helper(*args):
        if args not in results:
            results[args] = func(*args)
        return results[args]
    return helper

def divsum(n):
    sum = 1
    sqrtn = math.sqrt(n)
    for i in range(2, int(sqrtn)+1):
        if not n % i:
            sum += i
            if not i == sqrtn :
                sum += n / i
    return sum

def isprime(n):
    n = abs(n)
    sqrtn = math.sqrt(n)
    if n==2:
        return 1
    if not n&1:
        return 0
    for i in range(3, int(sqrtn)+1,2):
        if (n % i) == 0:
            return 0
    return 1

def genprimes(n):
    primes = set([])
    for i in range(2, n):
        if isprime(i):
            primes.add(i)
    return primes

def genprimes2(n, primes=None):
    start = 2
    if primes is not None:
        start = np.max(primes)+1
    else:
        primes = []
    for i in range(start, n):
        isprime=1
        s = int(math.sqrt(n))+1
        for p in primes:
            if (i % p) == 0:
                isprime = 0
                break
            if p > s:
                break
        if isprime:
            primes.append(i)
    return primes

def fac(n):
    if n <= 1:
        return 1
    else:
        return n * fac(n-1)

def factors(a):
    b = a
    f = set([])
    for i in primes:
        if not a % i:
            f.add(i)
            while not b%i:
                b = b / i
        if (i > np.sqrt(a)+1):
            break
    if b != 1:
        f.add(b)
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

def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return abs(a)

def bgcd(u, v):
    if (u == v):
        return u

    if (u == 0):
        return v

    if (v == 0):
        return u

    # look for factors of 2
    if not (u & 1): # u is even
        if (v & 1): # v is odd
            return gcd(u >> 1, v)
        else: # both u and v are even
            return gcd(u >> 1, v >> 1) << 1

    if not (v & 1): # u is odd, v is even
        return gcd(u, v >> 1)

    # reduce larger argument
    if (u > v):
        return gcd((u - v) >> 1, v)

    return gcd((v - u) >> 1, u)


def redfrac(a, b):
    d = gcd(a, b)
    while d > 1:
        a = a // d
        b = b // d
        d = gcd(a, b)
    return a, b

def mediant(n1,d1,n2,d2):
    return redfrac(n1+n2, d1+d2)


def setprimes(p):
    global primes
    primes = p

primes = genprimes2(1000)
