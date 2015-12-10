from euler import *

lim = 12000

ln = 1
ld = 3
hn = 1
hd = 2



def cntfrc(ln, ld, hn, hd):
    add = 0
    nn, dd = mediant(ln, ld, hn, hd)
    if dd <= lim:
        print ln, ld, nn, dd, hn, hd
        add += 1 + cntfrc(ln, ld, nn, dd) + cntfrc(nn, dd, hn, hd)
    else:
        return 0
    return add

while hd <= lim:
    hn, hd = mediant(ln, ld, hn, hd)

hn -= ln
hd -= ld

cnt = 1
print hn, hd
while 1:
    f = int((lim + ld) / hd)
    nn = f * hn - ln
    nd = f * hd - ld 
    if nn == 1 and nd == 2:
        break
    cnt += 1
#    print nn, nd
    ln = hn
    ld = hd
    hn = nn
    hd = nd

print cnt


#cnt = 0
#while 1:
#    nn, nd = mediant(ln, ld, hn, hd)
#    if nd > n:
#        print cnt, ":", ln, ld, ' | ', hn, hd, ' > ', nn, nd
#    if float(nn)/nd > 1./3:
#        hn = nn
#        hd = nd
#    else:
#        ln = nn
#        ld = nd
#    if nn == 1 and nd == 3:
#        break
#    cnt += 1

