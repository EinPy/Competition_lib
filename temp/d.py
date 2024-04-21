import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


# precomputing factorials modulo m up to some maxn

MAXN = 100000
MOD = 1000000007 
 
fact = [0] * MAXN
fact[0] = 1

#precompute factorials 
for i in range(1,MAXN):
    fact[i] = (fact[i-1] * i) % MOD

#precompute inverse factorials
#since (n+1)!= n!*(n+1)
# n! = (n+1)! * inv[n+1] % p

def mod_inv(a, p):
    return pow(a, p-2, p)

ifact = [0] * MAXN
ifact[0] = 1

ifact[MAXN - 1] = pow(fact[MAXN - 1], MOD - 2, MOD)

for i in range(MAXN - 2, 0, -1):
    ifact[i] = ifact[i+1] * (i+1) % MOD
    

def nCk(n, k):
    return (fact[n] * ifact[k] % MOD) * ifact[n-k] % MOD

sum = 0 

n, k = nl()
arr = nl()

arr.sort()

for i in range(n):
    if i + 1 >= k:
        sum  = (sum + nCk(i, k-1) % MOD * arr[i] % MOD) % MOD
        
print(sum)
