import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

import math

#debug print
db = False

def find_center(adj):
    #center should be node surrouded by the most nodes??
    #pop leaves succesively, last node should be center?
    #if something has indegree 1 it is a leaf
    #basically top_sort?
    in_deg  = [0] * len(adj)
    for u in adj:
        for v in u:
            in_deg[v] += 1
    
    q = deque([i for i in range(len(adj)) if in_deg[i] <= 1])

    last = 0
    while q:
        last = q.popleft()

        for v in adj[last]:
            in_deg[v] -= 1 
            if in_deg[v] == 1:
                q.append(v)
                
    if db: print("center node: ", last) 
    return last      

def bfs_cnt(adj, parent, start):
    q = [start]
    vis = [False for _ in range(len(adj))]
    vis[start] = True
    cnt = 1
    while q:
        q2 = []
        for u in q:
            for v in adj[u]:
                if not vis[v] and v != parent:
                    cnt += 1
                    vis[v] = True
                    q2.append(v)
        q = q2
    return cnt
        

def build_new_g(adj, s):
    q = [s]
    new_adj = [[] for _ in range(len(adj))]
    vis = [False for _ in range(len(adj))]
    vis[s] = True
    if db:print(adj)
    while q:
        q2 = []
        for u in q:
            for v in adj[u]:
                if not vis[v]:
                    vis[v] = True
                    q2.append(v)
                    new_adj[u].append(v)
        q = q2
    return new_adj


def solve(adj):
    start = find_center(adj)
    #easier to reconstruct tree from root than handling parent
    adj = build_new_g(adj, start)
    output_cords = [(-1,-1) for _ in range(len(adj))]
    output_cords[start] = (0,0)
    #alpha_1 > alpha_0
    if db: print(adj)
    def place_points(node, alpha_0, alpha_1):
        #find depth of points, weighted average of angle between all points

        x, y = output_cords[node]
        if db: print("at node", node, "with cords", x, y)
        if len(adj[node]) == 0: #only points to parent, and has already been placex
            if db: print("this is a leaf, do nothing")
            # #place in the middle of the bounds, and always use length one
            # theta = (alpha_1+ alpha_0) / 2
            # nx, ny = x + math.cos(theta), y + math.sin(theta)
            # output_cords[node] = (nx, ny)
            pass
        else:
            #check depths of all children, give them angle slices based weighted on children
            dpt = [0] * len(adj[node])
            for i in range(len(adj[node])):
                dpt[i] = bfs_cnt(adj, node, adj[node][i])
            tot = sum(dpt)
            lines = [alpha_0]
            cone = alpha_1 - alpha_0
            for i in range(len(dpt)):
                lines.append(lines[i] + (dpt[i] / tot) * cone)
            if db: print("angle boundries", lines)
            #place all pionts, and recurse on
            for i in range(len(dpt)):
                #take original point and place between bounds
                nx, ny = x + math.cos((lines[i] + lines[i+1]) / 2), y + math.sin((lines[i] + lines[i+1]) / 2)
                if db: print("placing node at", nx, ny)
                output_cords[adj[node][i]] = (nx, ny)
                #keep recursing
                place_points(adj[node][i], lines[i], lines[i+1])
                
    place_points(start, 0, 2 * math.pi)
    if db: print(output_cords)
    for x, y in output_cords:
        print("{:.12f} {:.12f}".format(x, y))
            

n = ni()
adj = [[] for _ in range(n)]

for _ in range(n-1):
    a, b = nl()
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)
    
solve(adj)