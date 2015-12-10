#!/usr/bin/python
a, b = 0, 1
i = 1
while a < 10**999:
    a, b = a + b, a
    i += 1
print a
print i
