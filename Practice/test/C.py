import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n = ni()
a = nl()
last = 0

found = True
for k in range(1, n//2+1):
    found = True
    vis = 0
    last= -1
    for i in range(k-1,n,k):
        vis += 1
        if a[i] > last:
            last = a[i]
        else:
            found = False
    if found and vis >= 2:
        print(k)
        break
    else:
        found = False
        
if not found:
    print("ABORT!")
        
    