import math

def contfrac(n):
    m = 0
    d = 1
    a0 = math.floor(math.sqrt(n))
    if a0**2 == n:
        return [n]
    a = a0
    
    an = [a0]

    cnt = 0
    while 1:
        m1 = d * a - m
        d1 = (n - m1**2) / d
        a1 = math.floor((a0+m1)/d1)
        if cnt == 0:
            start = [a1,m1,d1]
        
        a = a1
        m = m1
        d = d1
        
#        print a,m,d

        if cnt > 0 and [a,m,d] == start:
            return an
        an.append(int(a1))
        cnt += 1
    
cnt = 0
for i in range(2, 10001):
    cf = contfrac(i)
    l = len(cf) - 1 
    if l % 2:
        cnt += 1
        print cf, l

print cnt
