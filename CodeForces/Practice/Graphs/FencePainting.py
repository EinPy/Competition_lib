#solution to http://www.usaco.org/index.php?page=viewproblem2&cpid=944
import sys
from collections import *
sys.setrecursionlimit(10**5)
sys.stdin = open("fenceplan.in")
sys.stdout = open("fenceplan.out", "w")
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(cord, ajd):
    vis = [False for _ in range(len(adj))]
    vis[0] = True
    
    def dfs(s):
        q = deque([s])
        #vis[s] = True
        l, r, t, b = 1e9, -1, -1, 1e9
        visited = 1
        vis[s] = True
        x, y = cord[s]
        l = min(l, x)
        r = max(r, x)
        t = max(t, y)
        b = min(b, y)
        #print("starting at: ", s)
        while q:
            cur = q.popleft()
            for n in adj[cur]:
                if not vis[n]:
                    visited += 1
                    #print("visiting:", n)
                    x, y = cord[n]
                    l = min(l, x)
                    r = max(r, x)
                    t = max(t, y)
                    b = min(b, y)
                    vis[n] = True
                    q.append(n)
        if visited >= 2:
            per = (t - b) * 2 + (r - l) * 2
            return per
        return 1e9
    
    per = 1e19
    #print(vis)
    #print(adj)
    #print(cord)
    for i in range(len(ajd)):
        if not vis[i]:
            per = min(per,dfs(i))
    ##print(vis)
    print(per)
    


n, l = nl()
cord = [[] for _ in range(n+1)]
adj = [[] for _ in range(n+1)]
for _ in range(1,n+1):
    x, y = nl()
    cord[_] = [x,y]
for c in range(l):
    a, b = nl()
    adj[a].append(b)
    adj[b].append(a)

solve(cord,adj)