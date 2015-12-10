#!/usr/bin/python

val = [100, 50, 20, 10, 5, 2, 1]

p = [2, 0, 0, 0 ,0, 0, 0]
n = 2

def split(i):
    if i in (0, 2, 3, 5):
        p[i]   -= 1
        p[i+1] += 2
    elif i in (1, 4):
        p[i]   -= 1
        p[i+1] += 2
        if p[i+2] > 0:
            p[i+1] +=1
            p[i+2] -=1
        else:
            p[i+2] += 1

def collect(i):
    if i == 6:
        return
    x = 0
    for j in range(6,i,-1):
        x += p[j] * val[j]
        p[j] = 0
    
    for j in range(i,7):
        add = x // val[j]
        p[j] += add
        x -= add * val[j]
        if x == 0:
            break
        

while p[6]!= 200:
    i = 5
    while p[i] <=0: 
        i -= 1
        if i == -1: break
    
#    if i == -1:
#        i = 5
#        while p[i] < 1: 
#            i -= 1
#            if i == -1: break
#        split(i)
#        print "!",p
#        collect(i+1)
#        n += 1
#    else:
    split(i)
    collect(i+1)
    n += 1
        
#    print p
#    if n > 50:
#        break

print n
