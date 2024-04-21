import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n = ni()
g = [[] for _ in range(n)]
for i in range(n):
    p = nl()
    if len(p) > 1:
        for c in p[1:]:
            g[c-1].append(i)
            

in_deg = [0 for _ in range(n)]
for i in range(n):
    for dep in g[i]:
        in_deg[dep] += 1
        
q = []
sem = [[]]

tot = 0
for i in range(n):
    if in_deg[i] == 0:
        q.append(i)
        sem[-1].append(i)
        tot += 1
        
while q:
    q2 = []
    for course in q:
        for next in g[course]:
            in_deg[next] -= 1
            if in_deg[next] == 0:
                q2.append(next)
                tot += 1
    q = q2
    if q2:
        sem.append(q2)
        
if tot == n:
    print("Mogulegt!")
    print(len(sem))
    for i in range(len(sem)):
        print(len(sem[i]), end = " ")
        print(" ".join(map(str, [c+1 for c in sem[i]])))
else:
    print("Omogulegt!")
          
    