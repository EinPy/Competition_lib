#solution to https://cses.fi/problemset/task/1682
from ast import Str
import sys
from collections import *
from time import strptime
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]
    
 
n, m = nl()
n += 1
adj = [[] for i in range(n)]
adjR = [[] for i in range(n)]
for edge in range(m):
    a,b  = nl()
    adj[a].append(b)
    adjR[b].append(a)
    
s = []
vis = [False] * n
 
#first dfs, build stack based on exit order
def dfs1(i):
    vis[i] = True
    for u in adj[i]:
        if not vis[u]:
            dfs1(u)
    s.append(i)
    
for i in range(1,n):
    if not vis[i]:
        dfs1(i)
 
 
def dfs2(i):
    vis[i] = True
    for u in adjR[i]:
        if not vis[u]:
            dfs2(u)
            
vis = [False] * n
StrongComps = 0
out = []
for i in s[::-1]:
    if not vis[i]:
        StrongComps += 1
        out.append(i)
        dfs2(i)
        
        
if StrongComps == 1:
    print("YES")
else:
    print("NO")
    print(out[1], out[0])
