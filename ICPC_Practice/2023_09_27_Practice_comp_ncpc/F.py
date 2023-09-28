import sys, math
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

mod = 10**9 + 7

fact = [1]
tot = 1
for i in range(1, 2510):
    tot = (tot*i) % mod
    fact.append(tot)

n, k = nl()

def nCr(a, b):
    return fact[a]*pow(fact[a-b],-1,mod)*pow(fact[b],-1,mod) % mod
 
#print(nCr(7,0))       
tot = sum(pow(-1,k-t)*nCr(k,t)*t*pow(t-1,n-1,mod) for t in range(1,k+1))
print(tot%mod)