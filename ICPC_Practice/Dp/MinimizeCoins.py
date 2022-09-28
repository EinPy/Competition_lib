import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


n,m = nl()

co = nl()

dp = [1e7] * (m+1)
dp[0] = 0
for i in range(m):
    for c in co:
        if i + c <= m:
            dp[i+c] = min(dp[i+c], dp[i]+1)

if dp[m] == 1e7:
    print(-1)
else:
    print(int(dp[m]))
    
    