import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    pass


q = INP()
n = ni()
a = []
for _ in range(n):
    a.append(INP().split(","))

best = [0] * n
for i in range(n):
    ma = 0
    for j in range(n):
        diff = 0
        for alt in range(len(a[i])):
            #print(alt)
            if a[i][alt] != a[j][alt]:
                diff += 1
        ma = max(diff, ma)
    best[i] = ma
    
#print(a)
#print(best)
#print(best)
low = min(best)
#for _ in range(n):
   # print(a[_])
for ans in range(n):
    if best[ans] == low:
        print(','.join(a[ans]))