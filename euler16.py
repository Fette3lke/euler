#!/usr/bin/python
import math
n = [2]
for i in range(310):
    n.append(0)

extra = 0
for dum in range(999):
    for i in range(len(n)):
        d = n[i]*2
        n[i] = d % 10
        n[i] += extra
        extra= int(d/10)


for i in range(len(n)):
    print n[i],

print ""
print sum(n)

