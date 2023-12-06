import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

def ok(k, segs):
    #start at 0, jump no more than k steps
    #keep track of leftmost value and rightmost value
    mi, ma = 0,0
    for lb, rb in segs:
        #rightmost 
        #if segment to the right
        #3 cases
        # rght of ma
        #left of mi
        #somewhere in the middle
        if lb >= ma: #completally to the right
            if ma + k >= lb:
                ma = min(ma + k, rb)
                mi = lb
            else:
                return False #cannot reach next segment
        elif rb <= mi:
            #segment is complettaly to the left
            if lb - k <= rb:#reachable
                lb = max(lb - k, lb )
                rb = max(lb -k, rb)
        else:
            #some overlap between segments
                
            

def solve(n,a):
    l, r = 1, 10** 9 + 5
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if ok(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    print(ans)
            


t = ni()
for case in range(t):
    n = ni()
    a = []
    for _ in range(n):
        a.append(nl())
    solve(n,a)