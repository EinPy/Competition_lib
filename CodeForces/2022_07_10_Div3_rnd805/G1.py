import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


n = ni()
g = [[] for _ in range(n+1)]



    
            
            

for _ in range(n-1):
    u,v = nl()
    g[u].append(v)
    g[v].append(u)
    
#print(g)


def solve(n, g):
    def dfs(s,f, vis):
            stack = [s]
            vis[s] = True
            while stack:
                node = stack.pop()
                for v in g[node]:
                    if v == f:
                        vis[v] = True
                        return True, vis
                    #print(v, vis)
                    if vis[v] == -1:
                        stack.append(v)
                        vis[v] = True
            return  False, vis

    #print(n)
    vis = [-1 for _ in range(n+1)]
    #print(vis)
    while toVis:
        possible = False
        for i in range(len(toVis)):
            for j in range(len(toVis)):
                if i != j:
                    pos, temp = dfs(toVis[i],toVis[j],vis)
                    if pos == True:
                        vis = temp
                        toVis.pop(i)
                        possible = True
                        break
            break
        if not possible:
            return("NO")
            break
    return("YES")

q = ni()

for _ in range(q):
    l = ni()
    toVis = nl()
    print(solve(n,g))