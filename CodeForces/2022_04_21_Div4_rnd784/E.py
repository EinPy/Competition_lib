import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,arr):
    for i in range(n-1):
        for j in range(i,n):
            pass
            
    

t = ni()
for c in range(t):
    n = ni()
    arr = [None for _ in range(n)]
    for case in range(n):
        s = INP()
        arr[case] = s
    solve(n,arr)

            
        
         




