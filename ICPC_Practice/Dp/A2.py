import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n = ni()
sq = [0]
for _ in range(n):
    sq.append(ni())
    
been = [[-1 for _ in range(1001)] for _ in range(n+1)]

def rec(ind, j):
    if ind < 1 or ind > n:
        return 1000000
    if been[ind][j] != -1:
        return been[ind][j]
    if ind == n:
        return sq[ind]
    
    been[ind][j] =  sq[ind] + min(rec(ind - j, j), rec(ind+j+1,j+1))
    return been[ind][j]

#print(sq)
print(rec(2,1))