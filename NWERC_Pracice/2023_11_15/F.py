import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


def ok(mid, u, d, ud, dd):
    #check if weight next to it is same
    #check if in same rack
    cur = -1
    for w in u:
        if w > mid:
            if w in dd:
                return False
            if cur == -1:
                cur = w
            else:
                if cur == w:
                    cur = -1
                else:
                    return False
    for w in d:
        if w > mid:
            if cur == -1:
                cur = w
            else:
                if cur == w:
                    cur = -1
                else:
                    return False
    return True



def solve(u, d):
    #binary search possible without moving weight x
    l, r = 0, 10**9
    ud = {}
    dd = {}
    
    for w in u:
        if w not in ud:
            ud[w] = True
    for w in d:
        if w not in dd:
            dd[w] = True
    #print(ud, dd)
    
    mid = 0
    ans = -1
    
    #binary search for lower bound
    while l <= r:
        mid = (l + r) // 2
        #print(l, r, mid)

        if ok(mid, u, d, ud, dd):
            ans = mid
            r = mid-1
        else:
            l = mid+1
            
    print(ans)


t = ni()
u, d = nl(), nl()
solve(u, d)
