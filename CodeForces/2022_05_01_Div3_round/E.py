import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



import math

def solve(n,arr):
    best = 2e6
    cur = 2e6


    for i in range(n-1):
        f = max(arr[i], arr[i+1])
        s = min(arr[i], arr[i+1])

        #adjacent
        if f > 2 * s:
            cur = math.ceil(f/2)
        else:
            cur = math.ceil((s + f)/3)
        best = min(best, int(cur))
    
        best = min(best, int(cur))
        if i != 0:
            cur = 0
            side1 = min(arr[i-1],arr[i+1])
            side2 = max(arr[i-1],arr[i+1])
            cur += side1 + math.ceil((side2 - side1)/2)
            best = min(cur, best)

    arr.sort()
    a = (arr[0] + 1) //2 + (arr[1] + 1) // 2
        
    return min(int(a), best)
        
        
    

n = ni()
arr = nl()
print(solve(n, arr))