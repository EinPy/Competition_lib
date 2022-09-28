import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


#djikstra ashortest path in weighted graph. 
from heapq import heappush, heappop

def solve(n,g, k):
    
    vis = [False for _ in range(n+1)]
    #print(g)
    #find size of all components
    def dfs(i):
        vis[i] = True
        cnt = 1
        q = [i]
        while q:
            node = q.pop()
            for v in g[node]:
                if not vis[v]:
                    cnt += 1
                    q.append(v)
                    vis[v] = True
        return cnt
    count = 0
    for i in range(1,n+1):
        if not vis[i]:
            c = dfs(i)
            count += c ** k
    #print(count)
    tot = n ** k
    #print(tot)
    print((tot - count) % (10**9 + 7))
    
n, k = nl()
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = nl()
    if c == 0:
        g[a].append(b)
        g[b].append(a)
    
solve(n, g, k)
