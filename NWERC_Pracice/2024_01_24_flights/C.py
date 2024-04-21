import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

import math as m

R = 6381

#djikstra ashortest path in weighted graph. 
from heapq import heappush, heappop
# S: Start node
# G: [[(to_node, weight)]], for instance [[(1,3), (0,3), ...], [...], ...]
#return shortes dists to all
INF = 10**9
def djikstra (S, G):
    dists = {}
    for node in G.keys():
        dists[node] = INF
    heap = []
    heappush(heap, (0,S))
    dists[S] = 0
    
    while heap:
        d, u = heappop(heap)
        for v, c in G[u]:
            alt = d + c   + 100# cost per flight?
            if alt < dists[v]:
                dists[v] = alt
                heappush(heap, (alt, v))
                
    return dists

def xyz(f):
    phi, the = f
    return (R * m.sin(phi) * m.cos(the),
            R * m.sin(phi) * m.sin(the),
            R * m.cos(phi)
            )

def dot(A, B):
    return A[0]*B[0] + A[1] * B[1] + A[2] * B[2]

def sz(A):
    return m.sqrt(A[0]**2 + A[1] ** 2 + A[2] ** 2)

def anglebetween(A, B):
    return m.acos( dot(A, B) / (sz(A) * sz(B)))

n, M = nl()
s, t = INP().split()

dct = {}

for _ in range(n):
    a, b , c = INP().split()
    b = -1 * (float(b) - 90) * (m.pi / 180)
    c = (float(c) + 180) * (m.pi / 180)
    dct[a] = (b,c)
    
#create actual roads. 

g = defaultdict(list)

for _ in range(M):
    a, b = INP().split()
    #get distance, R times the angle
    A = xyz(dct[a])
    B = xyz(dct[b])
    theta = anglebetween(A, B)
    dist = abs(R * theta)
    g[a].append((b, dist))
    g[b].append((a, dist))
    
#do the shortest path
out = djikstra(s, g)[t]
if out==INF:
    print(-1)
else:
    print(out)
