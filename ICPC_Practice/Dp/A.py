import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n = ni()
sq = []
for _ in range(n):
    sq.append(ni())
    
been = [[-1 for _ in range(1001)] for _ in range(n)]

def rec(ind, l, c):
    if ind < 0:
        return 10000000
    if ind > n-1:
        return 10000000
    
    if l != 0:
        c += sq[ind]
    if been[ind][l] == -1:
        been[ind][l] = c
    else:
        if been[ind][l] <= c:
            return 10000000
        else:
            been[ind][l] = c
    if ind == n-1:
        return c
    
    #jump back
    #print(ind, l, c)
    return min(rec(ind + l + 1, l+1,c), rec(ind-l, l, c))
#print(sq)
print(rec(0,0,0))