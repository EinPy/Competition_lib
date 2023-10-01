import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


#Bfs to find distannce to all nodes in graph 
def bfs(Graph, S):
    q = deque([S])
    
    while q:
        q2 = []
        for u in q:
            for n in Graph[u]:
                if dists[n] == -1:
                    dists[n] = dists[u] + 1
                    q2.append(n)
        q = q2
    return dists


#group all bfs from leaf nodes into groups from where they terminate


A, B, E, P = nl()
#A, B interval
adj = [[] for _ in range(E)]
inDeg = [0 for _ in range(E)]
dists = [-1 for _ in range(E)]
leaves = []



#Bfs to find distannce to all nodes in graph 
def bfs(Graph, S):
    q = [S]
    dists[S] = 0
    while q:
        q2 = []
        for u in q:
            for n in Graph[u]:
                if dists[n] < dists[u] + 1:
                    dists[n] = dists[u] + 1
                    q2.append(n)
        q = q2

#E Employe, P edges
for _ in range(P):
    a, b = nl()
    adj[a].append(b)
    
for i in range(E):
    for j in adj[i]:
        inDeg[j] += 1
print(inDeg)
        
for n in range(E):
    if inDeg[n] == 0:
        leaves.append(n)
    
print(leaves)
for l in leaves:
    bfs(adj, l)
print("dist", dists)
counts = [0 for _ in range(E)]
for i in range(len(dists)):
    counts[dists[i]] += 1

Ap = 0
Aprom = True
Bp = 0  
Bprom = True
Np = 0
orgB = B
for i in range(E):
    if Aprom and counts[i] <= A:
        A -= counts[i]
        Ap +=counts[i]
    else:
        Aprom = False
        
    if Bprom and counts[i] <= B:
        B -= counts[i]
        Bp += counts[i]
    else:
        Bprom = False
    if dists[i] > orgB:
        Np += 1
        
print(Ap)
print(Bp)
print(Np)