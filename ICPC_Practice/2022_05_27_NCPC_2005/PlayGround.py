import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [float(_) for _ in INP().split()]


while True:
    n = ni()
    if n == 0:
        break
    a = nl()
    a.sort()
    if len(set(a)) != len(a):
        print("YES")
    else:
        found = False
        for i in range(n-1, -1, -1):
            tot = 0
            for j in range(i):
                tot += a[j]
            if tot >= a[i]:
                found = True
                break
            
        if found:print("YES")
        else:print("NO")
        