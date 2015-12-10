#!/usr/bin/python

limit = 100
v = []
for a in range (2,limit + 1):
    for b in range (2,limit + 1):
        v.append(a**b)

v.sort()
i=0
while i < len(v)-1:
    if v[i] == v[i+1]:
        v.pop(i+1)
#    print i
    else:
        i += 1
#print v 
print len(v)
