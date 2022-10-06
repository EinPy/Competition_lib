import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



n, w = nl()
g = [[] for _ in range(n+2)]
revG = [[] for _ in range(n+2)]
cap = [0] * (n+2)
cur = [0] * (n+2)
cap[0] = w

for i in range(1,n+1):
    to, ca, cu = nl()
    g[i].append(to)
    revG[to].append(i)
    cap[i] = ca
    cur[i] = cu
    
#find leafs
#Bfs to find distannce to all nodes in graph 
def bfs(Graph, S):
    q = [S]
    dists = [False for _ in range(len(Graph))]
    dists[S] = True
    leaves = []
    while q:
        q2 = []
        for u in q:
            if len(Graph[u]) == 0:
                leaves.append(u)
            for n in Graph[u]:
                if dists[n] == False:
                    dists[n] = True
                    q2.append(n)
        q = q2
    return leaves

leaves = bfs(revG, 0)
#print(g)
#print(bfs(revG, 0))

#print(g)
#print(leaves)
def ok(num):
    memo = {}
    pos = False
    #print(leaves)
    for l in leaves:
        #print(l)
        cu = 0
        while True:
            
            #print(l)
            if cu == 0:
                new = cu + cur[l] + num
            else:
                new = cu + cur[l]
            if l in memo and memo[l] >= new:
                break
            memo[l] = new
            if l == 0:
                break
            if new >= cap[l]:
                l = g[l][0]
                cu = new
            else:
                l = g[l][0]
                cu = 0
        if cu >= w:
            pos = True
            break
    if pos:
        return True
    else:
        return False
            

#Binary search for lower bound
def lower_bound(w):
    l, r, m = 0, 3*w, 0
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if ok(mid) or mid >= w:
            ans = mid
            r = mid-1
        else:
            l = mid + 1
    return ans

print(lower_bound(w))