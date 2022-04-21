import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]





def solve(trees):
    left = stay = right = trees
    cut = 0
    for i in range(len(trees)):
        
        
    pass


N = ni()
trees = [0] * N
for t in range(N):
    c, h = nl()
    trees[t] = [c,h]
 
#print(trees)
memo = [-1] * N
print(solve(trees))