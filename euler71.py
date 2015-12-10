from euler import *

setprimes(genprimes2(1000))

hn = 3
hd = 7
ln = 1
ld = 7

d = 1



while 1:
    n = hn + ln
    d = hd + ld
    if d < 1000000:
        ln = n
        ld = d
    else:
        print hn, '/', hd
        hn = n
        hd = d
        print ln, '/', ld
        break

print n, '/', d
    
