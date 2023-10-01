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
        leaves.append(n)
    if inDegRev[n] == 0:
        leavesRev.append(n)
        
def topSrt(Gr, S):
    q = deque(S)
    dists = [0 for _ in range(len(Gr))]
    while q:
        #get next node from q
        node = q.pop()
        #print(node)
        
        for n in Gr[node]:
            inDeg[n] -= 1
            dists[n] += dists[node] + 1
            if inDeg[n] == 0:
                #The node now has inDegree 0 and can be added to q
                q.append(n)
                
    return dists


        
            
    


#Bfs to find distannce to all nodes in graph 
def bfs(Graph, S):
    q = deque([S])
    dists = [-1 for _ in range(len(Graph))] 
    for l in S:
        dists[l] = 0
    while q:
        q2 = []
        for u in q:
            for n in Graph[u]:
                if dists[n] == -1:
                    dists[n] = dists[u] + 1
                    q2.append(n)
        q = q2
    return dists


vis = [False for _ in range(len(adj))]
pred = [0 for _ in range(len(adj))]
dists = [-1 for _ in range(E)]
succ = [0 for _ in range(len(adj))]

#start from leaves and go out with outdegree. 
def dfs(node):
    cnt = 1
    vis[node] = True
    for neighbour in adj[node]:
        if not vis[neighbour]:
            cnt += dfs(neighbour)
    succ[node] = cnt
    return cnt
            
for l in leaves:
    dfs(l, 1)
print(vis)
print()


print(inDeg)
print("leaves", leaves)
print("pred", topSrt(adj, leaves))
print("succ", topSrt(adjRev, leavesRev))



print(inDeg, leaves, inDeg)