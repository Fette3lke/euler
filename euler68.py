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

def rotate(mgon, i):
    tmp = mgon[:]
    for j in range(5):
        mgon[j] = tmp[(j+i)%5]
        mgon[j+5] = tmp[((j+i)%5)+5]
    return mgon


def check(mgon):
    s1 = mgon[0] + mgon[5] + mgon[6]
    s2 = mgon[1] + mgon[6] + mgon[7]
    if s1 != s2:
        return False
    s3 = mgon[2] + mgon[7] + mgon[8]
    if s1 != s3:
        return False
    s4 = mgon[3] + mgon[8] + mgon[9]
    if s1 != s4:
        return False
    s5 = mgon[4] + mgon[9] + mgon[5]
    if s1 != s5:
        return False
    i = mgon.index(min(mgon[0:5]))
    rotate(mgon, i)
    return int(str(mgon[0]) + str(mgon[5]) + str(mgon[6]) + str(mgon[1]) + str(mgon[6]) + str(mgon[7]) + str(mgon[2]) + str(mgon[7]) + str(mgon[8]) + str(mgon[3]) + str(mgon[8]) + str(mgon[9]) + str(mgon[4]) + str(mgon[9]) + str(mgon[5]) )


mgon = [9,8,7,6,5,4,3,2,1]

maxv=0
for p in perms(mgon):
    pmgon = p+[10]
    s = check(pmgon)
    if s:
        print pmgon, sum([pmgon[0], pmgon[5], pmgon[6]])
        if s > maxv:
            maxv = s

print maxv
