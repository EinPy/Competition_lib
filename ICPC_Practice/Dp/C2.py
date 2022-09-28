import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

t = ni()
p = []
tot = 0
for i in range(t):
    w = ni()
    p.append(w)
    tot += w
    
pos = [False for _ in range(4000)]
pos[0] = True
best = -1
for w in p:
    for i in range(4000-1,-1, -1):
        if pos[i]:
            if (i + w < 4000-1):
                pos[i + w] = True
            
for i in range(len(pos)):
    if pos[i]:
        if abs(1000 - i) <= abs(1000-best):
            best = i
            
print(best)