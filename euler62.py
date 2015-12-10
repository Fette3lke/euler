from itertools import count
from collections import defaultdict
import numpy as np

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

cubes = defaultdict(list)
minlen = 5

i = 0
for i in count(1):
    c = i**3
    sc = str(c)
    s = sum([int(j) for j in sc])
    ss= sum([int(j)**2 for j in sc])
    d = set(sc)
    
    cubes[s].append( [len(sc), sum([int(j) for j in list(d)]), ss, d, c])
    if len(str(c)) > 12:
        break


def recfunc(dd, lvl):
    tpl = []
    for k in dd:
        if len(dd[k])>=minlen:
            ndd = defaultdict(list)
            for ii in dd[k]:
                ndd[ii[0]].append(ii[1:])
            if lvl < 2:
                tpl += recfunc(ndd, lvl+1)
            else:
                tpl += [ndd]
    return tpl
            

candidates = recfunc(cubes, 0)
permcubes = []

for c in candidates:
    for n in c:
        if len(c[n]) >= minlen:
#            print n, len(c[n])
#            if n == 21:
#                print c[n]
            tpl = c[n]
            for i,t in enumerate(tpl):
                cnt = 0
                res = []
                for j in range(i, len(tpl)):
                    if t[0] == tpl[j][0]:
                        cnt += 1
                        res.append(tpl[j])

                if cnt >= minlen:
#                    print t
                    permcubes.append(t[-1])
#                    print "!"
                    for r in res:
#                        if t[-1] == 10175991463:
#                        print r
                        permcubes.append(r[-1])

print np.min(permcubes)
