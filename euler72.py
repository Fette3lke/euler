import numpy as np
from euler import *

def totient(n):
    fac = factors(n)
    p = 1
    for f in fac:
        p *= (1.-1./f)

    return np.round(n * p)

maxv = 20000
n = 1000000
totients = map(lambda x: totient(x), range(1, maxv+1))
totients = [0] + totients
fn = []
fnadd = 1

for i in range(maxv+1):
    fnadd += totients[i]
    fn.append(fnadd)

print 'Fn values hashed'

def divide(n):
    a = range(2,n+1)
    a = map(lambda x: int(n/x), a)
    return a

def repl(x):
    for i, e in enumerate(x):
        if e > maxv:
            x[i] = divide(e)
            repl(x[i])
        else:
#            0.5 * (e + 3) * 3  
#            x[i] = fn[e]
            x[i] = e

def calc(x):
    for i, e in enumerate(x):
        if type(e)==list:
            x[i] = calc(e)
        else:    
#    for i, e in enumerate(x):
            x[i] = fn[e]

    n = len(x) + 1
    return int(0.5 * (n+3) * n - sum(x))


t=divide(n)
repl(t)
print calc(t)

