#!/usr/bin/python
from euler import *

m = 0

for a in range(-999, 1000):
    for b in range(-999, 1000):
#        if not isprime(b):
#            continue
        i = 0
        while 1:
            n = i**2 + a * i + b
            if not isprime(n):
                break
            i += 1
        if i > m:
            m = i
            c = (a, b)

print m, c
