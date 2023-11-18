import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def bfs(g, s):
    q = [s]
    dist = [-1 for _ in range(len(g))]
    dist[s] = 0
    while q:
        # print(q)
        # print(dist)
        q2 = []
        for u in q:
            for v, d in g[u]:
                #print("to", v, "from" ,u, "dist", d)
                if dist[v] == -1:
                    dist[v] = dist[u] + d
                    q2.append(v)
        q = q2
    return dist
                

def solve(adj, revC, revI, sz, ic, cc):
    if ic == 0 or cc == 0:
        print("impossibe")
        return
    #find path from origin to all nodes
    d1 = bfs(adj, 0) # from start node
    d2 = bfs(revC,sz) # from coal
    d3 = bfs(revI, sz+1) #iron
    # print(adj)
    # print(rev)
    # print(d1)
    # print(d2)
    # print(d3)
    fnd = False
    bst = 10**9
    for i in range(sz):
        if d1[i] != -1 and d2[i] != -1 and d3[i] != -1:
            bst = min(bst, d1[i] + d2[i] + d3[i])
            fnd = True
    if fnd:
        print(bst)
    else:
        print("impossible")


nodes, Icnt, Ccnt = nl()
Iidx = nl()
Cidx = nl()

#g[i][j][c] = from node i to node j with weight c = 0 or 1
g = [[] for _ in range(nodes+2)] #g[n] = coal, g[n+1] = iron
revC = [[] for _ in range(nodes+2)] #g[n] = coal, g[n+1] = iron
revI = [[] for _ in range(nodes+2)] #g[n] = coal, g[n+1] = iron

#add edges with weight 0 to all coal and iron nodes, in both rev and normal
for v in Iidx:
    idx = v - 1
    # g[idx].append((nodes+1, 0))
    # g[nodes + 1].append((idx, 0))
    
    revI[idx].append((nodes + 1, 0))
    revI[nodes + 1].append((idx, 0))

    
#same for coal to idx n

for v in Cidx:
    idx = v - 1
    # g[idx].append((nodes, 0))
    # g[nodes].append((idx, 0))
    
    revC[idx].append((nodes, 0))
    revC[nodes].append((idx, 0))
    
#build graphs
for i in range(nodes):
    p = nl()
    if p[0] != 0:
        for v in p[1:]:
            g[i].append((v-1, 1))
            revC[v-1].append((i, 1))
            revI[v-1].append((i, 1))
            
solve(g, revC, revI, nodes, Icnt, Ccnt)
    
    