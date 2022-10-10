import sys
from collections import *
from turtle import done
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

N = ni()

edge = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b=nl()
    edge[a].append(b)
    edge[b].append(a)

w = [-1]*(N+1)

visited = [False]*(N+1)

def weight(n):
    if w[n]!=-1:
        return w[n]
    
    visited[n]=True
    tot = 1
    for e in edge[n]:
        if not visited[e]:
            tot+=w[e]
    w[n]=tot
    return w[n]

weight(1)

adjW= []
root = 1
done = False
while not done:
    adjW = []

    for e in edge[root]:
        adjW.append((w[e],e))
    adjW.sort()
    s = sum(list(map(lambda x: x[0],adjW)))
    if 2*adjW[-1][0]-2> s:
        w[root] -= adjW[-1][0]
        w[adjW[-1][1]] += w[root]
        root = adjW[-1][1]
    else: done = True


    

out = []
#Bfs to find distannce to all nodes in graph 
def bfs(s):
    q = [s]
    dists = [-1 for _ in range(len(edge))]
    out.append(s)
    while q:
        q2 = []
        for u in q:
            for n in edge[u]:
                if dists[n] == -1:
                    dists[n] = dists[u] + 1
                    q2.append(n)
                    out.append(n)
        q = q2
    for i in dists:
        if i > 1:
            return True
    return False
    
        
    

if bfs(root):
    print("YES")
    print(' '.join(list(map(str,out))))
else:
    print("NO")