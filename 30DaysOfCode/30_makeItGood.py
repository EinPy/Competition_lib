import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(n, arr):
    if n < 3:
        return 0
    
    fM = n-1
    while fM - 1 >= 0 and arr[fM-1] >= arr[fM]:
        fM -= 1
        
    while fM - 1 >= 0 and arr[fM-1] <= arr[fM]:
        fM -= 1
    
    return fM



t = ni()
for case in range(t):
    n = ni()
    arr = nl()
    print(solve(n, arr))