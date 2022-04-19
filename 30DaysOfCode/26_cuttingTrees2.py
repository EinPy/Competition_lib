import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]
 
 
 
 
 
def solve(trees,memo, tot = 0, cur = 0):
    if len(trees) == 0:
        return 0
    if memo[cur] != -1:
        return memo[cur]

    
    
    for t in range(cur, len(trees)):
        p, h = trees[t]
        if t == 0:
            tot += 1
        else:
            if p-h > trees[t-1][0]: 
                tot += 1
            else:
                #noCut = trees
                #cutrightgt: trees[]
                if t == len(trees)-1:
                    tot += 1
                    return tot
                    
                elif p + h < trees[t+1][0]:
                    cutRight = trees[:]
                    cutRight[t][0] = p + h
                    memo[t] = max(solve(cutRight,memo, tot+1, t+1),
                                  solve(trees,memo, tot, t+1))
                    return memo[t]
                else:
                    #cannot cut right or left
                    continue
                
    return max(tot, memo[len(trees)-1])
    
    
N = ni()
trees = [0] * N
for t in range(N):
    c, h = nl()
    trees[t] = [c,h]
 
#print(trees)
memo = [-1] * N
print(solve(trees, memo))