#!/usr/bin/python
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

fac = [factorial(i) for i in range(10)]

def sumfactorial(n):
    sum = 0
    while n>0:
        sum += fac[n % 10]
        n = int (n/10)
    return sum

sum = 0
for i in range(10, 1000000):
    if i == sumfactorial(i):
        sum += i
        print i, sum

