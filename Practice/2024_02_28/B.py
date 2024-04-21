import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    pass


n = ni()
arr = nl()

dp = [[0 for _ in range(n)] for _ in range(2)]
dp[0][0] = arr[0]
dp[1][0] = 0

#row 0 is do, row 1 is skip

for i in range(1, n):
    dp[0][i] = min(dp[1][i-1] + arr[i], dp[0][i-1] + arr[i])
    dp[1][i] = dp[0][i-1] + 0
    
print(min(dp[1][n-1], dp[0][n-1]))
    