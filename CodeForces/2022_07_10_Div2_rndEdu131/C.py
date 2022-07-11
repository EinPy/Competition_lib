import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,m, a):
    cnt = [0 for _ in range(m+1)]
    for i in range(m):
        cnt[a[i]] += 1
    
    def ok(t):
        if t == 0:
            return False
        totLeft = 0
        freeT = 0

        for i in range(1,n+1):
            w = min(t, cnt[i])
            freeT += (t - w) // 2
            totLeft += cnt[i] - w
        if freeT >= totLeft:
            return True
        else:
            return False
    
    l, r, m = 0, 2 * m + 1, 0
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if ok(mid):
            ans = mid
            r = mid-1
        else:
            l = mid + 1
    return ans


t = ni()
for case in range(t):
    n, m = nl()
    a = nl()
    print(solve(n,m, a))