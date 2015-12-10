from euler import *
import numpy as np
primes = genprimes2(100000)
npprimes = np.array(primes)

#s = np.array([0,1,2,3,4])
s = np.array([0,1,2,3])

def isprime(n, p = primes):
    n = abs(n)
    sqrtn = math.sqrt(n)
    for i in p:
        if (n % i) == 0:
            return 0
        if i > int(sqrtn)+1:
            break
    return 1

def isprime2(n):
    if n in primes:
        return True
    else:
        return False

def next(s):
    for i in range(len(s)):
        n = s[i] + 1
        if n not in s:
            s[i] = n
            s[0:i] = np.arange(i)
            break
    return s

def permutations(n, j):
    ret = []    
    for i in range(len(n)):
        if j == 1:
            ret.append(n[i])
        else:
            for p in permutations(n[i+1:], j-1):
                app = np.array([n[i]])
                app = np.append(app, p)
                ret.append(app)
    return ret

def tuples(n):
    ret = []
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            ret.append([n[i], n[j]])
    return ret

def check(a, b):
    if not isprime(int(str(a) + str(b))):
        return False
    if not isprime(int(str(b) + str(a))):
        return False
    return True

def tcheck(t, b):
    if type(t) == int:
        t = [t]
    for a in t:
        if not check(a,b):
            break
    else:
        return True
    return False


i = 3
ntpl = 5
good = [[] for j in range(ntpl)]
good[0] = [3]
while 1:
    prime = primes[i]
    new = []
#    for g in (good[0]):
#        if j == 1:
#            break
    for t in good[0]:
        if tcheck(t, prime):
            add = [prime]
            if type(t) == int:
                add.append(t)
            else:
                add.extend(t)
            good[1].append(add)
            new.append(t)
    
    tpl = []
    further = set([])
    for n in tuples(new[:]):
        if check(n[0], n[1]):
            add = set([prime, n[0], n[1]])
            further.add(n[0])
            further.add(n[1])
#            if n[0] in new:
#                new.remove(n[0])
#            if n[1] in new:
#                new.remove(n[1])
            good[2].append(add)
            tpl.append(add)

    
    tpl3 = []
    further3 = set([])
    for n in further:
        for t in tpl:
            if not n in t:
                if tcheck(t, n):
                    add = set(t)
                    add.add(n)
                    add.add(prime)
                    if add not in good[3]:
                        good[3].append(add)
                        tpl3.append(add)
                    further3.add(n)
#    further = further2
#    tpl = tpl3

    tpl4 = []
    further4 = set([])
    for n in further3:
        for t in tpl3:
            if not n in t:
                if tcheck(t, n):
                    add = set(t)
                    add.add(n)
                    add.add(prime)
                    if add not in good[4]:
                        good[4].append(add)
                        tpl4.append(add)
                    further4.add(n)
            
    good[0].append(prime)
    i += 1
#    if not (i % 20):
#        print len(good[1]), i, prime, len(new)
#    if (prime == 673):
#        break
    if len(good[4]):
        print good[4], sum(good[4][0]), further4, prime
        break


        
