import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n = ni()
dp = [0] * (n+10)
dp[0] = 1
for i in range(n):
    for j in range(1,7):
        dp[i+j] += dp[i]
        dp[i+j] = dp[i+j] % (1e9 + 7)
        
print(int(dp[n]))
