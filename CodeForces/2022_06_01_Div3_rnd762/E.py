import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    possible = True
    a.sort()
    cnt = Counter(a)
    ops = 0
    out = []
    if cnt[0] >= 1:
        out.append(cnt[0])
    else:
        possible = False
        print(' '.join(map(str,[0] + [-1]*(n))))
        return 
    
    ops += cnt[0]
    print(a)
    for i in range(1,n+1):
        ops -= cnt[i-1]
        if a[i-1] > i-1:
            possible = False
        ops +=  (i-1) - (a[i-1]) + cnt[i]
        if not possible:
            out.append(-1)
        if possible:
            out.append(ops)
    print(' '.join(map(str,out)))

t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)