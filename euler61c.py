#solution taken from forum user chenaren

from itertools import count
from collections import defaultdict
import sys


def four_digit_gen(func):
  for n in count(1):
    val = str(func(n))
    if len(val) > 4:
      break
    if len(val) == 4:
      yield val

funcs = (lambda n: n * (n + 1) / 2,
         lambda n: n * n,
         lambda n: n * (3 * n - 1) / 2,
         lambda n: n * (2 * n - 1),
         lambda n: n * (5 * n - 3) / 2,
         lambda n: n * (3 * n - 2))

nums_all = map(lambda f: list(four_digit_gen(f)), funcs)

maps_all = []
for nums in nums_all:
  m = defaultdict(list)
  for n in nums:
    m[n[:2]].append(n[2:])
  maps_all.append(m)


def find_cycle(cur, accu, start, maps):
  if not maps and cur == start:
    print accu
    sys.exit(0)
  for i, m in enumerate(maps):
    if cur in m:
      for nex in m[cur]:
        find_cycle(nex, accu + int(cur + nex), start,
                   maps[:i] + maps[i + 1:])


for i in xrange(10, 100):
  i = str(i)
  find_cycle(i, 0, i, maps_all)
