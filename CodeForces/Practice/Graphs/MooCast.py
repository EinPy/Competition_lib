#solution tohttp://www.usaco.org/index.php?page=viewproblem2&cpid=668
import sys
from collections import *
sys.setrecursionlimit(10**5)
sys.stdin = open("moocast.in")
sys.stdout = open("moocast.out", "w")
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

import math


def solve(n,a):
    length = n
    
    def dfs(s):
        q = deque([s])
        vis = [False for _ in range(length)]
        vis[s] = True
        cnt = 1
        while q:
            cur = q.popleft()
            for n in graph[cur]:
                if not vis[n]:
                    cnt += 1
                    q.append(n)
                    vis[n] = True
        return cnt
    
    most = 0
    for i in range(n):
        #if not vis[i]:
        most = max(most, dfs(i))
    print(most)


t = ni()
graph = [[] for _ in range(t)]
nodes = [[] for _ in range(t)]
for case in range(t):
    x, y, p = nl()
    nodes[case] = [x,y,p]
    
    
for i in range(t-1):
    for j in range(i+1,t):
        #a to b
        #print(nodes[i], nodes[j])
        d = math.sqrt(abs(nodes[i][0] - nodes[j][0])**2 + abs(nodes[i][1] - nodes[j][1])**2)
        #d = abs(nodes[i][0] - nodes[j][0]) + abs(nodes[i][1] - nodes[j][1])
        if d <= nodes[i][2]:
            graph[i].append(j)
        if d <= nodes[j][2]:
            graph[j].append(i)
#print(graph)
            
solve(t, graph)