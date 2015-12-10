#!/usr/bin/python
exp = []
for i in range(10):
    exp.append(i**5)

def sume5(n):
    sum = 0
    while n>0:
        sum += exp[n % 10]
        n = int(n/10)
    return sum

#for i in range (10**6):
sum = 0
for i in range (10, 10**7):
    dum = sume5(i)
    if i == dum:
        sum += dum
        print i, sum


