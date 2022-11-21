import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve():
    n = ni()
    g = []
    for l in range(n):
        g.append(list(map(int,list(INP()))))
    #print(g)
    sets = [[] for _ in range(n)]
    sets[-1] = [i for i in range(1,n+1)]
    ##print(sets)
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
             if g[i][j] == 1:
                #print(i, j, sets[j][:-1:1])
                 #set i subset of set j
                if sets[j] != []:
                    sets[i] = sets[j][:-1]
                else:
                    sets[i].pop()
                
    for s in sets:
        print(len(s), ' '.join(map(str,s)))

t = ni()
for case in range(t):
    solve()