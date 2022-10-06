import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


n = ni()
g = []
for _ in range(n):
    g.append(INP())
mod = 1e9 + 7
    
dp = [[0 for _ in range(n)] for _ in range(n)]


for i in range(n):
    if g[0][i]== ".":
        dp[0][i] =1 
    else:
        break
    
for i in range(n):
    if g[i][0] == ".":
        dp[i][0] =1 
    else:
        break

for r in range(1,n):
    for c in range(1,n):
        if g[r][c] == ".":
            newT = 0
            if g[r-1][c] == ".":
                newT += dp[r-1][c]
            if g[r][c-1] == ".":
                newT += dp[r][c-1]
            dp[r][c] = newT % mod
print(int(dp[n-1][n-1]))