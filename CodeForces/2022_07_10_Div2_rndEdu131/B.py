import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    pass


t = ni()
for case in range(t):
    n = ni()
    out = []
    cur = 1
    seen = {0:True}
    for i in range(1,n+1):
        cur = i
        while cur <= n:
            if cur not in seen:
                out.append(cur)
                seen[cur] = True
                cur *= 2
            else:
                break
            
            
    print(2)
    print(' '.join(map(str,out)))