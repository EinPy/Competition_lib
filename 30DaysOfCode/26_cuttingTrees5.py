import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(trees):
    n = len(trees)
    if n < 3:
        return n
    
    mem = [[-1 for _ in range(n)] for _ in range(2)]
    
    def dfs(prev,i):
        
        if i >= n-1:
            return 0
        
        pos, h = trees[i]
#        print(prev,pos, h)
        
        if pos - h > prev:
            return dfs(pos, i+1) + 1
        elif pos + h < trees[i+1][0]:
            return max(dfs(pos+h,i+1) + 1 ,dfs(pos,i+1))
        else:
            return dfs(pos,i+1)
        
    return dfs(trees[0][0],1) + 2
    
    




N = ni()
trees = [0] * N
for t in range(N):
    c, h = nl()
    trees[t] = [c,h]
 
#print(trees)
memo = [-1] * N
print(solve(trees))