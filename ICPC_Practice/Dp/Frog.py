import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


n = ni()
s = nl()
s += [0, 0]
dp = [1e10] * (n + 4)
dp[0] = 0

for i in range(n):
    dp[i+1] = min(dp[i+1], dp[i] + abs(s[i+1]- s[i]))
    dp[i+2] = min(dp[i+2], dp[i] + abs(s[i] - s[i+2]))
print(dp[n-1])
