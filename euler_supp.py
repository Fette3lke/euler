#!/usr/bin/python
import math
import numpy as np
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

def genprimes3(n):
    if n<2:
        return None
    primes = [ i for i in range(2,n) ]
    i = 0
    k = 0
    sn = math.sqrt(n)
    while i <= sn:
        i = primes[k]
        j = i * i
        while j < n:
            try:
                primes.remove(j)
            except ValueError:
                pass
                
            j += i
        k += 1
    return primes
