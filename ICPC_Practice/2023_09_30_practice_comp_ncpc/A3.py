import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]




A, B, E, P = nl()

#A, B interval
adj = [[] for _ in range(E)]
adjRev = [[] for _ in range(E)]
inDeg = [0 for _ in range(E)]
inDegRev = [0 for _ in range(E)]

leaves = []
leavesRev = []
roots = []
rootsRev = []



#E Employe, P edges
for _ in range(P):
    a, b = nl()
    adj[a].append(b)
    adjRev[b].append(a)
    
    
for i in range(E):
    for j in adj[i]:
        inDeg[j] += 1
    for j in adjRev[i]:
        inDegRev[j] += 1

        
for n in range(E):
    if inDeg[n] == 0:
        roots.append(n)
    if inDegRev[n] == 0:
        rootsRev.append(n)



vis = [False for _ in range(E)] 
dists = [-1 for _ in range(E)]
succ = [0 for _ in range(len(adj))]

#start from roots, count successors. 
def dfs1(node, seen):
    cnt = 1
    seen = seen | node
    vis[node] = True
    for neighbour in adj[node]:
        if not vis[neighbour]:
            sub =  dfs1(neighbour, seen)
            
    succ[node] = len(seen)
    return seen


#start from leaves, count parents
vis = [False for _ in range(E)] 
pred = [0 for _ in range(len(adj))]
def dfs2(node):
    cnt = 1
    vis[node] = True
    for n in adjRev[node]:
        if not vis[n]:
            cnt += dfs2(n)
    pred[node] = cnt
    return cnt

for r in roots:
    dfs1(r)
    
print(succ)
    
for r in rootsRev:
    dfs2(r)

print(pred)
