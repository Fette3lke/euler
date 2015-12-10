#!/usr/bin/python
def pal10(n):
    s = str(n)
    for i in range(len(s)):
        if s[i] != s[len(s)-i-1]:
            return 0
    return 1

def pal2(n):
    x = n
    y = 0
    while x > 0:
        y <<= 1
        if x&1:
            y |= 1
        x >>= 1
    if y == n:
        return 1
    return 0

sum = 0
for i in range(1,10**6):
    if pal10(i) and pal2(i):
        print i
        sum += i

print sum

