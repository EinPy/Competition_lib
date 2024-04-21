import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

n, h = nl()

#use a prefix array, then find the min height
 
 
arr = [0 for _ in range(h+2)]
for row in range(n):
    sz = ni()
    if row % 2 == 0:
        arr[0] += 1
        arr[sz+2]-=1
        
    else:
        arr[-1] -= 1
        arr[-sz] += 1
        
pref = [0 for _ in range(h)]
#print(arr)
cur = arr[0]
for i in range(h):
    cur += arr[i+1]
    pref[i] = cur 
    
#print(pref)
best  = min (pref)
print (best, pref.count(best))