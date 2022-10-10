import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


n = ni()
p = []
for _ in range(n):
    p.append(ni())
    
m = 100
hasB = False
stocks = 0
for i in range(n-1):
    #print(hasB, m, stocks)
    if not hasB:
        if p[i+1] > p[i]: #buy
            if m >= p[i]:
                hasB = True
                #print("money", m)
                stocks = m // p[i]
                #print(p[i], stocks)
                m -= stocks * p[i]
    if hasB:
        if p[i+1] < p[i]: #sell
            hasB = False
            m += stocks * p[i]
            stocks = 0
    #print(hasB, m, stocks)

if hasB:
    m += p[-1] * stocks

print(m)
