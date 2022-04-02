import sys

from numpy import True_
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)
#code

def solve(n,graph,Ff):
    totFf = 0
    leafs = [True_ for _ in range(n)]
    for e in graph:
        leafs[graph[e]] = False
    l = []
    for i in range(leafs):
        if leafs[i] == True:
            l.append(i)
            


    vis = [False for _ in range(len(graph))]
    for i in l:
        if leafs[i]:
            totFf = max(bfs(graph,i,Ff, vis), totFf)
    print(totFf)
    

#Bfs to find distannce to all nodes in graph 
def bfs(Graph, S,Ff, vis):
    q = [S]
    vis[S] = True
    best = S
    while q:
        q2 = []
        for u in q:
            if not vis[u]:
                if Graph[u] == 0:
                    return best
                vis[u] = True
                best = max(best,u)
                q2.append(Graph[u])
        q = q2
    return best




T = int(input())
for case in range(1,T+1):

    n = int(input())
    Ff = list(map(int,input().split()))
    graph = list(map(int,input().split()))

    print(f'Case #{case}: ', end = '')
    solve(n,graph,Ff)
