import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def run():
    l, d, n = nl()
    pos = []
    for _ in range(n):
        pos.append(ni())
        
    pos.append(-d + 6)
    pos.append(l + d - 6)
        
    possible = 0
    pos.sort()
    for i in range(n+1):
        diff = pos[i+1] - pos[i]
        #print(diff)
        possible += diff // (d) - 1
        
    #print(pos)
    print(possible)

run()