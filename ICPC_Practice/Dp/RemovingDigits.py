import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



t = ni()
dp = [2e6] * (t +1)
dp[t] = 0
for i in range(t, -1, -1):
    dig = list(map(int,set(list(str(i)))))
    for d in dig:
        if i - d >= 0:
            dp[i-d] = min(dp[i-d], dp[i] + 1)
print(int(dp[0]))