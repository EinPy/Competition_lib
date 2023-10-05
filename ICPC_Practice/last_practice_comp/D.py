import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n, p = nl()
arr = sorted(nl())
#print(arr)
add = 0
for i in range(len(arr)):
    d = p * (i+1)
    if d > arr[i]:
        #print(d, arr[i], d - arr[i])
        add = max(d - arr[i], add)
        
print(add+arr[0])