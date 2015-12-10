#!/usr/bin/python
d = []
for i in range(0,200000):
    d.append(str(i))

s = "".join(d)
print len(s)

p = 1
for i in range (7):
    p *= int(s[10**i])
    print i, 10**i, s[10**i]

print p
