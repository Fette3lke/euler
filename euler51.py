from euler import *
import numpy as np

def dim(a):
    return len(str(a))

def digit(a, b):
    return int(str(a)[b])

def repl(a, b):
    ret = []
    for i in range(10):
        add = a
        add = np.array(list(str(add)))
        add[b] = str(i)
        if add[0] != "0":
            add = int("".join(add))
            ret.append(add)
    return ret

def positions(n):
    p = []
    l = np.array(list(str(n)))
    for i in range(4):
        b = np.arange(dim(n))[l == str(i)]
        if len(b):
            p.append(b.tolist())
    return p
        
def permutations(n, j):
    ret = []    
    for i in range(len(n)):
        if j == 1:
            ret.append(n[i])
        else:
            for p in permutations(n[i+1:], j-1):
                app = [n[i]]
                if type(p) == int:
                    app.append(p)
                else:
                    app.extend(p)
                ret.append(app)
    return ret


def check(n):
    pos = positions(n)
    for p in pos:
        for i in range(len(p)):
            perms = permutations(p, i+1)
            for per in perms:
                c = repl(n, per)
                s = sum([isprime(j) for j in c])
                if s > 6:
                    print c
                    print s

i = 56001
nextprint = 100000
while 1:
    if isprime(i):
        check(i)
        if i > nextprint:
            print i
            nextprint *= 2
    i += 2
    
