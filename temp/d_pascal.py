import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]




MOD = 1000000007 
MAXN = 100001
MAXK = 55

psc = [[0 for _ in range(MAXK+1)] for _ in range(MAXN+1)]

psc[0][0] = 1

for n in range(1, MAXN):
    psc[n][0] = 1
    for k in range(1, min(n+1, MAXK)):
        psc[n][k] = (psc[n - 1][k - 1] + psc[n-1][k]) % MOD
        
sum = 0 

n, k = nl()
arr = nl()

arr.sort()

for i in range(n):
    if i + 1 >= k:
        sum  = (sum + psc[i][k-1]% MOD * arr[i] % MOD) % MOD
        
print(sum)
