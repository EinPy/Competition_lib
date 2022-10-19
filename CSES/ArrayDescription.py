from lzma import MODE_FAST
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


#solution to https://cses.fi/problemset/task/1746

n, lim = nl()
a = nl()

MOD = 1e9 + 7

#each 0 detemines an unkonwn value
#array with dp[row][col] with col being wich elemennt and 
#row being the value fo the thing?
dp = [[0 for _ in range(n+1)] for _ in range(lim+1)]
best = 0



if a[0] == 0:
    for j in range(1,lim+1):
        dp[j][0] = 1
else:
    dp[a[0]][0] = 1

# for l in dp:
#     print(l)
    
for i in range(1, n):
    if a[i] == 0:
        for v in range(1,lim+1):
            dp[v][i] += dp[v][i-1] % MOD
            if v-1 >= 1:
                dp[v][i] += dp[v-1][i-1] % MOD
            if v+1 <= lim:
                dp[v][i] += dp[v+1][i-1] % MOD
                
            dp[v][i] = dp[v][i] % MOD
    else:
        v = a[i]
        dp[v][i] += dp[v][i-1] % MOD
        if v-1 >= 1:
            dp[v][i] += dp[v-1][i-1] % MOD
        if v+1 <= lim:
            dp[v][i] += dp[v+1][i-1] % MOD
            
        dp[v][i] = dp[v][i] % MOD
# for l in dp:
#     print(l)
            
#number of ways is number of ways to reach all possible end values
ans = 0
for i in range(lim+1):
    ans += dp[i][n-1] % MOD
print(int(ans %MOD) )
