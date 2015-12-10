from collections import defaultdict
from scipy.misc import factorial

fac = [int(factorial(i)) for i in range(10)]
counts = [0 for i in range(61)]
known = dict()

def facsum(n):
    sum = 0
    for i in str(n):
        sum += fac[int(i)]
    return sum

def cycle(n, p=False):
    nums = [n]
    if n in known:
        return known[n]
    while 1:
        n = facsum(n)
        if n in known:
            l = len(nums)
            for i, j in enumerate(nums):
                known[j] = known[n] + l - i
            return known[n] + l
        if p:
            print n
        if n in nums:
            l = len(nums)
            ind = nums.index(n)
            for i, j in enumerate(nums[0:ind]):
                known[j] = l - i
            for j in nums[ind:]:
                known[j] = len(nums[ind:])
            return len(nums)
        else:
            nums.append(n)

for i in range(1000000):
    l = cycle(i)
    counts[l] += 1

print counts[60]

