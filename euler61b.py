import numpy as np

def tri(n):
    return n*(n+1)/2

def squ(n):
    return n**2

def pen(n):
    return n*(3*n-1)/2

def hex(n):
    return n*(2*n-1)

def hep(n):
    return n*(5*n-3)/2

def oct(n):
    return n*(3*n-2)

nfuncs = 6

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

def getunion(s, b):
    ret = set([])
    for i in range(len(s)):
        if b[i]:
            ret.update(s[i])
    return ret

def perms(v):
    ret = []
    if len(v) == 1:
        return [v]
    for i in range(len(v)):
        cp = v[:]
        cp[0] = v[i]
        cp[i] = v[0]
        for p in perms(cp[1:]):
            add = [cp[0]]
            if type(p) == int:
                add.append(p)
            else:
                add.extend(p)
            ret.append( add )
    return ret
#    return ret

def cycle(v):
    b = True
    for i in range(nfuncs):
        j = (i+1) % nfuncs
        if (v[i] % 100) != (v[j] // 100):
            b = False
            break
    return b

def possible(v, n):
    p = set([])
    for i in v:
        p.add(i % 100)
        p.add(i // 100)
        if len(p) > n:
            return False
    return True
    
def numpairs(v):
    p = set([])
    for i in v:
        p.add(i % 100)
        p.add(i // 100)
    return len(p)


def anycycle(v):
    for p in perms(v[1:]):
        check = [v[0]]
        check.extend(p)
        if cycle(check):
            return True
    return False

def clean(o, n):
    repeat = True
    while repeat:
        repeat = False
        for i in range(n):
            if len(o[i]) == 1:
                for j in range(n):
                    if i != j:
                        for e in o[i]:
                            if e in o[j]:
                                o[j].remove(e)
                                repeat = True

    return o

def check(n, res):
    o = []
    for i in range(len(res)):
        if n in res[i]:
            o.append(i)
    return o
        

funcs = [tri, squ, pen, hex, hep, oct]
results = [set([]) for i in range(nfuncs)]
go = np.ones(nfuncs)

n = 0
while np.sum(go):
    for i in range(nfuncs):
        if go[i]:
            res = funcs[i](n)
            if res < 10000:
                if res >= 1000:
                    results[i].add(res)
            else:
                go[i] = 0
    n += 1

#fronts = [set([]) for i in range(nfuncs)]
#ends = [set([]) for i in range(nfuncs)]
#for i in range(nfuncs):
#    for j in results[i]:
#        fronts[i].add(j //100)
#        ends[i].add(j % 100)

for n in range(10):
    fronts = [set([]) for i in range(nfuncs)]
    ends = [set([]) for i in range(nfuncs)]
    for i in range(nfuncs):
        for j in results[i]:
            fronts[i].add(j //100)
            ends[i].add(j % 100)

    for i in range(nfuncs):
        j = (i+1) % nfuncs
        cpends = ends[:]
        cpends.remove(ends[i])
        endscheck = set.union(*cpends)
        cpfronts = fronts[:]
        cpfronts.remove(fronts[i])
        frontscheck = set.union(*cpfronts)
        ends[i].intersection_update(frontscheck)
        fronts[i].intersection_update(endscheck)

    if n == 9:
        break
    for i in range(nfuncs):
        res = results[i].copy()
        for j in res:
            front = j // 100
            end = j % 100
            if front not in fronts[i] or end not in ends[i]:
#                pass
                results[i].remove(j)
        

#for i in range(nfuncs):
#    results[i].intersection_update(maybe)

npresults = np.array([np.array(list(results[i])) for i in range(nfuncs)])
    


num = 0

b = [0 for i in range(nfuncs)]
stop = False
while not stop:
    tpl = []
    for i in range(nfuncs):
        tpl.append(npresults[i][b[i]])

#    if possible(tpl, nfuncs):
#        if anycycle(tpl):
#            stop = True
#            print tpl

    for i in range(nfuncs-1, -1, -1):
        if numpairs(tpl[i:]) > nfuncs:
            b[i] += 1
            break
    else:
        if anycycle(tpl):
            stop = True
            print tpl
        else:
            b[0]+=1
        
#    b[0] += 1
    for i in range(nfuncs):
        if b[i] >= len(npresults[i]):
            b[i] = 0
            if (i+1) == nfuncs:
                stop = True
                break                    
            b[i+1] += 1
    num += 1
    if not (num % 500000):
        print b[nfuncs-1]

#print num
    
#
#for i in range(nfuncs):
#    b = [0 for i in nfuncs]
#cycle()
