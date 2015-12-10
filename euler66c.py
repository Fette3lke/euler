from math import *

def initialise():
    global a,p,q,P,Q,gn
    a = [int(sqrt(D))]      # a0
    p = [a[0]]              # p0
    q = [1]                 # q0
    P = [0]                 # P0
    Q = [1]                 # Q0
    P.append(a[0])          # P1
    Q.append(D - a[0]*a[0]) # Q1
    a.append((a[0] + P[1])/Q[1]) # a1
    p.append(a[0]*a[1]+1)   # p1
    q.append(a[1])          # q1
    gn = 1

# P, Q, a, p, q
def step():
    global gn
    gn += 1
    n = gn
    P.append(a[n-1]*Q[n-1]-P[n-1])
    Q.append((D - P[n]*P[n])/Q[n-1])
    a.append((a[0] + P[n]) / Q[n])
    p.append(a[n]*p[n-1]+p[n-2])
    q.append(a[n]*q[n-1]+q[n-2])

def minusOnePow(n):
    if n % 2: return -1
    return 1

def check():
    n = gn
    if a[n] == 2*a[0]: return True
    return False

# returns the smallest x that solves for this D (global)
def solve():
    initialise()
    while 1:
        if check():
            k = gn-1
            if k % 2:
                return p[k]
            else:
                # um, need 2k+1 but only have k+1 steps so far
                for i in range(0,k): step()
                return p[2*k+1]
        step()

(bestx,bestD) = (0,0)
for D in range(2,1000):
    Ds = int(sqrt(D))
    if Ds*Ds == D: continue # no square D
    x = solve()
    if x > bestx: (bestx,bestD) = (x,D)

print  "got %d for D = %d" % (bestx,bestD)
