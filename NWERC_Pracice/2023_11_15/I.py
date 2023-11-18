import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


def bfs(Graph, S, dists, idx):
    q = [S]
    dists[S][idx] = 0
    while q:
        q2 = []
        for u in q:
            for n, d in Graph[u]:
                if dists[n][idx] == -1:
                    dists[n][idx] = dists[u][idx] + d
                    q2.append(n)
        q = q2
    return dists



def solve(adj, ra,n):
    #find distance to all nodes, find shortest distance from coal to iron
    dists = [[-1,-1,-1] for _ in range(len(adj))] #[origin, coal, iron]
    #find distance to all nodes from origin
    dists = bfs(adj,0,dists, 0)
    #find distance to all nodes from coal in rev graph
    dists = bfs(ra, n, dists, 1)
    #find distance to all nodes from iron in rev graph
    dists = bfs(ra, n+1, dists, 2)
    
    #find cell with minimal sum of distances
    cur = 10**15
    found = False
    #print(dists)
    for j in range(len(dists) - 2):
        o, c, i = dists[j]
        if o != -1 and c != -1 and i != -1:
            found = True
            cur = min(cur, o + i + c)
    #print(adj)
    #print(dists)
    if found:
        print(cur)
    else:
        print("impossible")


    


n, i ,c = nl()
coal = nl()
iron = nl()

# from to weight
adj = [[] for _ in range(n+2)] #cell n = coal master, cell n+1 = iron master
#all coal cells and all iron cells have a road to master cell, two way
ra = [[] for _ in range(n+2)]
for u in coal:
    #print("from,", u, "to ", n)
    adj[u-1].append((n,0))
    adj[n].append((u-1,0))
    
    ra[u-1].append((n,0))
    ra[n].append((u-1,0))
    
for u in iron:
    adj[u-1].append((n+1,0))
    adj[n+1].append((u-1,0))
    
    ra[u-1].append((n+1,0))
    ra[n+1].append((u-1,0))


for i in range(n):
    v = nl()
    if v[0] != 0:
        for j in range(1,len(v)):
            adj[i].append((v[j]-1,1))
            ra[v[j]-1].append((i,1))

           

solve(adj,ra,n)
    