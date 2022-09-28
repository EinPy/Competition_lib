import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]
 
 
#lesson learned, it is not enought that a component of the graph
#is bipirtite for the entire graph to be bipirtite


n, m = nl()
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = nl()
    g[a].append(b)
    g[b].append(a)
    
#print(g)
#bipartness check
#do a bfs
visited = [False for _ in range(n+1)]
R, B = {}, {}
def bfs(s):
    q = [s]
    visited[s] = True
    cnt = 0
    isB = True
    R[s] = True
    while q:
        q2 = []
        if cnt % 2 != 0:
            isB = False
        else:
            isB = True
        cnt += 1
        
        for node in q:
            #print(node, isB)
            #print(R,B)
            for v in g[node]:
                #print("neightobur: ", v)
                if visited[v]:
                    if isB:
                        if v in R:
                            #print("here")
                            return False
                    else:
                        if v in B:
                            return False
                else:
                    if isB:
                        B[v] = True
                    else:
                        R[v] = True
                    visited[v] = True
                    q2.append(v)
        q = q2
    ##print("what")
    #print(R, B)
    return True
 
f = True
for i in range(1, n+1):
    if not visited[i]:
        if len(g[i]) == 0:
            visited[i] = True
        else:
            if not bfs(i):
                f = False
    
if not f:
    print(-1)
else:
    #print(S, S2)
    print(len(R.keys()))
    for p in R.keys():
        print(p, end = " ")
    print()
    print(len(B.keys()))
    for p in B.keys():
        print(p, end = " ")