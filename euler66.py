import numpy as np

def dioph(x, d):
    pass


maxv = 1
maxx = 1

maxy = 0
miny = 0

maxsqr=100000
minsqr=1

ncheck = 250
fails = [i for i in range(1,ncheck) if (np.sqrt(i)!=np.floor(np.sqrt(i)))]

while 1:
    
    sqrs = np.array([i**2 for i in range(minsqr, maxsqr)])
    sqrs_m1 = sqrs - 1
    print 'maxsqrs: %d | minsqrs %d | len(sqrs) %d' % (maxsqr, minsqr, len(sqrs))

#    minsqr=maxsqr
    maxsqr *= 2

#    sqrs = np.array(sqrs)
    
#    sqrs_m1 = sqrs[:] - 1
#    ssqrs_m1 = set(sqrs_m1[:])

    msqrs = [0]
    #for i in range(1,10000):
    #    m = i * sqrs[:]
    #    msqrs.append(m)

    cnt = 0
    
    cpfails = fails[:]
    fails = []
    for i in cpfails:
        
        m = (i * sqrs)
        inter = np.intersect1d(m, sqrs_m1, assume_unique=True)
        if not len(inter):
            print "!!!! no solution found"
            cnt += 1
            fails.append(i)
            continue
        j = np.min(inter)
        y = np.sqrt(j / i)
        x = np.sqrt(j+1)

        if x > maxx:
            print 'D = %10d | x = %10d | y = %10d' % (i, x, y)
            maxv = i
            maxx = x
            if y > maxy:
                maxy = y

    print 'failed: ', fails
    if len(fails) == 0:
        break
    minsqr = int(maxy)

    tmp = (maxsqr - 1) / min(fails)
    if tmp > minsqr:
        minsqr = int(tmp)

print "maximal x: %d for D = %d" % (maxx, maxv)
