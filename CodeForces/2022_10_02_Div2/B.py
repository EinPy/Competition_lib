import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

import math

#Binary search for lower bound
def lower_bound(a, x):
    l, r, m = 0, x, 0
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if mid != 0 and math.ceil(x / mid) < 2 *a:
            ans = mid
            r = mid-1
        else:
            l = mid + 1
    return ans



def solve(n,a):
    #max < min * 2
    a.sort()
    ops = 0
    for i in range(n):
        ans = lower_bound(a[0], a[i])
        #print(ans)
        ops += ans - 1
    print(ops)


t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)