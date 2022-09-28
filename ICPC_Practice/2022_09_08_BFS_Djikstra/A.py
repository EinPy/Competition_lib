import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

people = {"PAUL_ERDOS": 0}
inputs = []

while True:
    try:
        l = INP().split()
        inputs.append(l)
    except:
        break
    
for l in inputs:
    for p in l:
        if p not in people:
            people[p] = len(people)    


g = [[] for _ in range(len(people) + 10)]


#Bfs to find distannce to all nodes in graph 
def bfs(s):
    q = deque([s])
    vis = [-1 for _ in range(len(g))]
    vis[s] = 0
    while q:
        q2 = []
        for u in q:
            for n in g[u]:
                #print(n)
                if vis[n] == -1:
                    vis [n] = vis[u] + 1
                    q2.append(n)
        q = q2
    return vis



for l in inputs:

    for a in l:
        g[people[l[0]]].append(people[a])
        g[people[a]].append(people[l[0]])
        
        
        
dists = bfs(0)
for l in inputs:
    print(l[0], end = " ")
    d = dists[people[l[0]]]
    if d == -1:
        print("no-connection")
    else:
        print(d)