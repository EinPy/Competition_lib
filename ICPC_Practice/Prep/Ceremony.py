import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n = ni()
H = nl()
H.sort(reverse=True)


best = n

for no_vert in range(n):
    cur = no_vert + H[no_vert]
    best = min(best, cur)
    
print(best)
        