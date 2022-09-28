import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


nC, t = nl()
coin = nl()
dp = [0 for _ in range((t+1))]
dp[0] = 1
mod = 1e9+7

for i in range(t):
    for c in coin:
        if i + c <= t:
            dp[i+c] += dp[i]
            dp[i+c] = dp[i+c] % mod
        
print(int(dp[t]))

