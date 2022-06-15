import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


def solve(n,m, ajd):
    #print(adj)
    def dfs(s):
        adj[s][0] =  0
        q = [s]
        while q:
            nd = q.pop()
            for v in adj[nd][1]:
                #print(adj)
                if adj[v][0] == -1:
                    adj[v][0] = opp(ajd[nd][0])
                    q.append(v)
   
    dfs(1)
    for node in range(1,n+1):
        if adj[node][0] == -1:
            dfs(node)
    #check
    for node in range(1,n+1):
        possible = False
        for neigh in adj[node][1]:
            if adj[neigh][0] == opp(adj[node][0]):
                possible = True
        if not possible:
            print("Impossible")
            return
    out = []
    for c in adj:
        if c[0] == 0: out.append("pub")
        elif c[0] == 1: out.append("house")
    print(' '.join(map(str, out)))
        
    
    
    
    
def opp(num):
    if num == 1: return 0
    else: return 1
                
            

n, m = nl()
adj = [[-1,[]] for _ in range(n+1)]
for c in range(m):
    x, y = nl()
    adj[x][1].append(y)
    adj[y][1].append(x)
#print(adj)
solve(n,m,adj)