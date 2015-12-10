from euler import *
import numpy as np
mmax = 880
limit = 1500000
counts = np.zeros(limit+1)

cnt = 1
for m in range(1, mmax+1):
    for n in range(1, m):
        if not ((m - n) % 2):
            continue
        if bgcd(n, m) == 1:            
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            pl = a + b + c
            l = pl
            k = 1
            while l <= limit:
                counts[l] += 1
                k += 1
                l = k * pl
        cnt +=1
