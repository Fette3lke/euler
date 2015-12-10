#!/usr/bin/python

m  = 0
mi = 0
mv = []
for i in range(2,1000):
    rest = 1.
    d = [1.]
    rv= []
    j = 0
    cycle = 0
    while rest > 0:
        rest *= 10
        div = rest // i
        rest -= div * i
        if rest in rv:
            cycle = j - rv.index(rest)
            break
        rv.append(rest)
        d.append(div)
        j += 1
    mv.append(cycle)


m = max(mv)
i = mv.index(m)

print i+2, m
