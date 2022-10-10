import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


n, k = nl()
prob = list(map(float, INP().split()))
prob.sort(reverse=True)

#print (n, k, prob)
dp = [[0 for _ in range((i+3) * 2)] for i in range(n+2)]
#for l in dp:
    #print(l)
    
best = 0
dp[0][0] = 1
for r in range(n+1):
    dp[r][-r] = 1
for i in range(1,n+1):
    
    for j in range(-i+1,i+1):
        #print(i, j, prob[i-1])
        dp[i][j] =  prob[i-1] * dp[i-1][j-1] +(1-prob[i-1]) * dp[i-1][j+1]
        if j >= k:
            best = max(best, dp[i][j])

print("{:.10f}".format(best))
#for l in dp: print(l)