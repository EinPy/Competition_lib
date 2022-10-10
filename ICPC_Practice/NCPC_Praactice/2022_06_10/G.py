import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



import math 






n, p = nl()
# P(1) - P(<1)

best = 0
cur = 0
a = 1* p / (n + 1)
for i in range(p -1): # imax = p-2
    a *= (n-i) / (n + 1 -(i +1))
    
best = a
#print(a)
for x in range(2, 10* n):
    a = a * (1/(x-1)) * (x/(n +x)) * (n + (x-1) - (p-1))
    best = max(a, best)
    #if x < 10:
        #print(x, a)
    
print(best)