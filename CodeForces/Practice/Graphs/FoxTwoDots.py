#https://codeforces.com/problemset/problem/510/B
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n, m = nl()
g = []
for i in range(n):
    g.append(list(INP()))
    
#print(g)

#problem is you cannot backtrack
v = [[False for _ in range(m)] for _ in range(n)]

def bfs(i, j):
    t = g[i][j]
    v[i][j] = True
    q = [(i, j)]
    usedEdges = {}
    while q:
        #for l in v:
        #    print(l)
        #print()
        rr, cc = q.pop()
        for r, c in [(rr+1, cc), (rr -1, cc), (rr, cc+1), (rr,cc-1)]:
            if r >= 0 and r < n and c >= 0 and c < m:
                if g[r][c] == t:
                    if (rr, r, cc, c) not in usedEdges:
                        if v[r][c]:
                            #print(r, c)
                            return True
                        v[r][c] = True
                        q.append((r,c))
                        usedEdges[(rr,r,cc,c)] = True
                        usedEdges[(r,rr,c,cc)] = True
    return False

def run():
    for i in range(n):
        for j in range(m):
            if not v[i][j]:
                if bfs(i, j):
                    return "Yes"
    return "No"

print(run())