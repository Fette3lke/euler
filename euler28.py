#!/usr/bin/python
dim = 1001
x = int(dim/2)
y = x

grid = [[0 for col in range(dim)] for row in range(dim)]

d=0
for i in range(1,dim*dim+1):
    grid[x][y] = i
    if i == dim**2:
        break
    if d==0:
        x += 1
        if not grid[x][y+1]:
            d=1
    elif d==1:
        y += 1
        if not grid[x-1][y]:
            d=2
    elif d==2:
        x -= 1
        if not grid[x][y-1]:
            d=3
    elif d==3:
        y -= 1
        if not grid[x+1][y]:
            d=0

sum = 0
for i in range(dim):
    sum += grid[i][i] + grid[dim-i-1][i]
    
sum -= 1
print sum
