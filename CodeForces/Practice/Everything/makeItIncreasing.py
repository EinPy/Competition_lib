import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(n,arr):
    
    ops = 0
    for i in range(n-2, -1, -1):
        while arr[i] >= arr[i+1] and arr[i] != 0:
            arr[i] = arr[i] // 2
            ops += 1
        if arr[i+1] == 0:
            return -1
        
    return ops




t = ni()
for case in range(t):
    n = ni()
    arr = nl()
    print(solve(n,arr))