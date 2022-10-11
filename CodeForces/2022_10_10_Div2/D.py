import sys
from collections import *
from turtle import right
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    if n == 1:
       print(0)
       return
    def rec(l,r):
        #print(l, r)
        global pos
        if r == l+1:
            if a[l] > a[r]:
                #print("returning: ", [min(a[l],a[r]), max(a[l],a[r]), 1])
                return [min(a[l],a[r]), max(a[l],a[r]), 1]
            return [min(a[l],a[r]), max(a[l],a[r]), 0]
        
        mid = (l+r) // 2
        left = rec(l, mid)
        rig = rec(mid+1, r)
        
        ops = left[2] + rig[2]
        
        if left[0] < rig[0] and left[1] > rig[0]:
            ops = -1e9
        if left[0] > rig[0] and rig[1] > left[0]:
            ops = -1e9
        if left[0] > rig[0]:
            ops += 1
            
        return [min(left[0], rig[0]), max(left[1], rig[1]), ops]

    ans = rec(0, n-1)
    #print(ans)

    if ans[-1] >= 0: print(ans[-1])
    else:
        print(-1)

t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)