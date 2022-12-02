
import sys
from collections import *
from heapq import heappop as pop, heappush as push
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

def inv(i, C):
    return i // (C - 1), i % C

def gc(r, c, C):
    return r*C + c

def solve(r0, c0, G, R, C):
    r0 -= 1
    c0 -= 1
    
    N = R*C
    INF = 10**18
    dist = [[INF]*C for _ in range(R)]
    pq = []
    
    def add(r, c, dst):
        if dst < dist[r][c]:
            dist[r][c] = dst
            push(pq, (dst, r, c))
    add(r0, c0, 1)
    best = INF
    while pq:
        D, r ,c = pop(pq)

        if G[r][c] == 'D':
            if r == 0 or r == R - 1 or c == 0 or c == C - 1:
                return D
        if D != dist[r][c]: continue
        
        if r < R - 1 and G[r + 1][c] != '#':
            if G[r + 1][c] == 'c':
                add(r + 1, c, D + 1)
            else:
                add(r + 1, c, D)
        
        if r > 0 and G[r - 1][c] != '#':
            if G[r - 1][c] == 'c':
                add(r - 1, c, D + 1)
            else:
                add(r - 1, c, D)
            
        if c < C - 1 and G[r][c + 1] != '#':
            if G[r][c + 1] == 'c':
                add(r, c + 1, D + 1)
            else:
                add(r, c + 1, D)
            
        if c > 0 and G[r][c - 1] != '#':
            if G[r][c - 1] == 'c':
                add(r, c - 1, D + 1)
            else:
                add(r, c - 1, D)
    
    return best
        
R, C = nl()
grid = []
for _ in range(R):
    grid.append(list(INP()))
r0, c0 = nl()
print(solve(r0, c0, grid, R, C))