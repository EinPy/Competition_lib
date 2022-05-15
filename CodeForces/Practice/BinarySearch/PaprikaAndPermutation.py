import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


#Binary search for lower bound

def solve(n,a):
    ops = 0
    a.sort()
    seen = {}
    low = 1
    #print(a)
    for i in range(n):
        #no operations
        if a[i] not in seen and a[i] <= n:
            seen[a[i]] = True
        else:
            while low in seen:
                low += 1
            if low < a[i] / 2 :
                ops += 1
                seen[low] = True
            else:
                #print(i, low)
                return -1

    return ops


t = ni()
for case in range(t):
    n = ni()
    a = nl()
    print(solve(n,a))