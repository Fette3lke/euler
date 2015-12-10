target = 10**6

def phi_sum(limit):
   phi = range(limit + 1)
   for n in xrange(2, limit + 1):
      if phi[n] == n:
         for k in xrange(n, limit + 1, n):
            phi[k] = phi[k] / n * (n-1)
   return sum(phi) - 1
   
      
print phi_sum(target)
