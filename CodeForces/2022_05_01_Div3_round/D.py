import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(n, arr):
    c = [0 for _ in range(n)]
    #print(n)
    start = 0
    if n % 2 != 0:
        c[0] = arr[0]
        start = 1

    for i in range(start,n-1,2):
        if arr[i] < arr[i+1]:
            c[i] = arr[i]
            c[i+1] = arr[i+1]
        else:
            c[i] = arr[i+1] 
            c[i+1] = arr[i]  
            
    for i in range(1,n):
        if c[i-1] > c[i]:
            return "NO"

    return "YES"

        


t = ni()
for case in range(t):
    n = ni()
    arr = nl()
    print(solve(n, arr))