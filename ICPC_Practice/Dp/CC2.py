import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


n, targ = nl()
coins = nl()
coins = coins
mod = 1e9+7

dp = [[0 for _ in range(targ +1)] for _ in range(n+1)]
dp[0][0] = 1

for c in range(1, n+1):
    for i in range(targ + 1):
        dp[c][i] = dp[c-1][i]
        left = i - coins[c-1]
        if left >= 0:
            dp[c][i] = (dp[c][i] + dp[c][left]) % mod
print(int(dp[n][targ]))