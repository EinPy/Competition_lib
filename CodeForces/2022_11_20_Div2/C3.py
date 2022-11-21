import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve():
    n = ni()
    mat = []
    for l in range(n):
        mat.append(list(map(int,list(INP()))))
    #print(mat)
    out = [[] for _ in range(n)]
    for i in range(n):
        out[i].append(i+1)
        for j in range(n):
            if mat[i][j] == 1 and i != j:
                out[j].append(i+1)
                
    for l in out:
        print(len(l), ' '.join(map(str,l)))
                
    

t = ni()
for case in range(t):
    solve()