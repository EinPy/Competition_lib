#https://cses.fi/problemset/task/1623
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(n, a):
    w1, w2 = 0, 0
    
    def dfs(i, w1, w2):
        if i >= n:
            return abs(w2 - w1)
        
        return min(dfs(i+1, w1 + a[i], w2),dfs(i+1, w1, w2 + a[i]))
    
    
    print(dfs(0, w1, w2))

t = ni()
a = nl()
solve(t, a)