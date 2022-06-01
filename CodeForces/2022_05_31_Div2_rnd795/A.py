import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    
    odd, even = 0, 0 
    for i in range(n):
        if a[i] % 2 == 0:
            even += 1
        else:
            odd += 1
            
    print(min(odd, even))
        
        


t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)