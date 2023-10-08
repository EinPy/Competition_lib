import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

depth_graph = []

def isPrime(N):
    if N < 2: return False
    if N%2 == 0: return N == 2
    mx = min(int(N**.5) + 2, N)
    for i in range(3, mx, 2):
        if N % i == 0: return False
    return True

def compute_primes():
    i = 1
    primes = []
    while len(primes) < 69:
        if isPrime(i):
            primes.append(i)
        i += 1
    return primes

def dfs_depth(G, i, e):
    if final_graph[i] != -1:
        max_depths = -70
    else:
        max_depths = 0

    for v in G[i]:
        if v != e:
            if final_graph[v] == -1:
                max_depths = max(max_depths, dfs_depth(G, v, i) + 1)
            else:
                max_depths = max(max_depths, dfs_depth(G, v, i))

    depth_graph[i] = max_depths

    return max_depths

final_graph = []

def dfs_label(G, i, p, e):
    if len(G[i]) == 1 and i != 0:
        return

    max_idx = -1
    for k in G[i]:
        if k != e:
            if max_idx == -1:
                max_idx = k
            elif depth_graph[k] > depth_graph[max_idx]:
                max_idx = k
    # print(i, max_idx)
    if final_graph[max_idx] == -1:
        final_graph[max_idx] = final_graph[i] * p
    dfs_label(G, max_idx, p, i)

def solve(G, N):
    primes = compute_primes()

    i = 0
    while -1 in final_graph:
        dfs_depth(G, 0, -1)
        # print(depth_graph)
        dfs_label(G, 0, primes[i], -1)
        # print(final_graph)
        
        # print(final_graph)
        i += 1
    
    print(' '.join(map(str, final_graph)))
    
    
        
        

N = ni()
G = [[] for _ in range(N)]
depth_graph = [0] * N
final_graph = [-1] * N
final_graph[0] = 1
for _ in range(N - 1):
    u, v = nl()
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
    

solve(G, N)
