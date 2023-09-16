import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    seen = 1
    #print(a)
    for num in a:
        #print(num)
        if num == seen:
            seen += 1

    return n - (seen -1)
        
        
        


t = ni()
for case in range(t):
    n = ni()
    a = nl()
    print(solve(n,a))