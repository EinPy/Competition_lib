import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(trees):
    n = len(trees)
    if n == 0:
        return 0
    
    count = 0
    for t in range(n):
        if t == 0 or t == n-1:
            count += 1
        else:
            pos, h = trees[t]
            if pos-h > trees[t-1][0]:
                count += 1
            elif pos + h < trees[t+1][0]:
                count += 1
                trees[t][0] = pos + h
            else:
                #don't cut tree
                continue
    return count
    
        


N = ni()
trees = [0] * N
for t in range(N):
    c, h = nl()
    trees[t] = [c,h]
 
#print(trees)
memo = [-1] * N
print(solve(trees))