import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



import math

def solve(n, arr):
    mi, ma = 2e10, 0
    
    for i in range(n):
        mi = min(mi, arr[i])
        ma = max(ma, arr[i])
        
    miA, maA = 0, 0
    
    for i in range(n):
        if arr[i] == mi:
            miA += 1
        if arr[i] == ma:
            maA += 1
    
    
    print(ma - mi, end = " ")
    if miA == 1:
        print(maA)
    elif maA == 1:
        print(miA)
    elif mi == ma:
        print(math.comb(miA, 2))
    else:
        print(int(maA * miA))



t = ni()
arr = nl()
solve(t, arr)