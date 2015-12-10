#!/usr/bin/python
import math
def d(n):
    sum = 1
    sqrtn = math.sqrt(n)
    for i in range(2, int(sqrtn)+1):
        if not n % i:
            sum += i
            if not i == sqrtn :
                sum += n / i
    return sum


sum = 0 

for i in range(2, 10000):
    a = d(i)
    b = d(a)
    if i == b and not a == i:
        sum += a
#        sum += i
        print a, i

print sum
