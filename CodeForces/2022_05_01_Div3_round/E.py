import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(n,arr):
    best = 2e6
    cur = 2e6

    s1, s2 = 2e6, 2e6
    for i in range(n-1):
        f = max(arr[i], arr[i+1])
        s = min(arr[i], arr[i+1])
        if s < s1:
            s2 = s1
            s1 = s
        elif s < s2:
            s2 = s
        #print(s, f)
        cur = ((2 * s) // 3) + (f - s) // 2
        #print(cur)
        if (f-s) % 2 == 1:
            cur += 1
        #print(cur)
        best = min(best, cur)
        
    if s1 %2 == 0:
        s1 = s1 // 2
    else:
        s1 = (s1 // 2) + 1
    if s2 % 2 == 0:
        s2 = s2 // 2
    else:
        s2 = (s2 //2) + 1
        
    return min(s1 + s2, best)
        
        
    

n = ni()
arr = nl()
print(solve(n, arr))