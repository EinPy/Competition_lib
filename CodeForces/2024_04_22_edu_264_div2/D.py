import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


# precomputing factorials modulo m up to some maxn

MAXN = 5001
MOD = 998244353 
 
fact = [0] * MAXN
fact[0] = 1

#precompute factorials 
for i in range(1,MAXN):
    fact[i] = (fact[i-1] * i) % MOD

def mod_inv(a, p):
    return pow(a, p-2, p)

ifact = [0] * MAXN
ifact[0] = 1

ifact[MAXN - 1] = pow(fact[MAXN - 1], MOD - 2, MOD)

for i in range(MAXN - 2, 0, -1):
    ifact[i] = ifact[i+1] * (i+1) % MOD

n = ni()
a = nl()
a.sort()

for i in range(n):
    