import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]




n = ni()
a = nl()

best = 1e9
bI = -1
for i in range(n - 2):
    if max(a[i], a[i+2]) < best:
        best = max(a[i], a[i+2])
        bI = i
print(bI+1, best)