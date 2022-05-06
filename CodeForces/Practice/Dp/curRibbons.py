import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(n, ribs):
    a, b, c = ribs
    memo = {}

    def dfs(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n < 0:
            return -1e9
        
        
        memo[n] = max(1 + dfs(n-a), 1 + dfs(n-b), 1 + dfs(n-c))
        return memo[n]
    
    print(dfs(n))


n, a, b, c = nl()
solve(n, [a,b,c])