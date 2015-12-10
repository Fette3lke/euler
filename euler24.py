#!/usr/bin/python

n = []

for a in range(10):
    p = [a]
    for b in range(10):
        if b not in p:
            p.append(b)
        else:
            continue
        for c in range(10):
            if c not in p:
                p.append(c)
            else:
                continue            
            for d in range(10):
                if d not in p:
                    p.append(d)
                else:
                    continue                
                for e in range(10):
                    if e not in p:
                        p.append(e)
                    else:
                        continue
                    for f in range(10):
                        if f not in p:
                            p.append(f)
                        else:
                            continue
                        for g in range(10):
                            if g not in p:
                                p.append(g)
                            else:
                                continue
                            for h in range(10):
                                if h not in p:
                                    p.append(h)
                                else:
                                    continue
                                for i in range(10):
                                    if i not in p:
                                        p.append(i)
                                    else:
                                        continue
                                    for j in range(10):
                                        if j not in p:
                                            p.append(j)
                                            l = len(p)
                                            num = 0
                                            for x in range(l):
                                                num += 10**(l-x-1) * p[x]
                                            n.append(num)
                                            p.pop()
                                    p.pop()
                                p.pop()
                            p.pop()
                        p.pop()
                    p.pop()
                p.pop()
            p.pop()
        p.pop()
        print len(n)
        if len(n) > 10**6: break;
    p.pop()

print len(n)
#print n
print n[999999]



                        

