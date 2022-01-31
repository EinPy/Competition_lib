import sys

def setupInputOutputSublime():
    import os

    if os.name == 'nt':
        sys.stdout = open("C:\\Temp\\output.txt", mode = 'w')
        sys.stdin = open("C:\\Temp\\input.txt", mode = 'r')
setupInputOutputSublime()
from math import sqrt

itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)


n, m = list(map(int,input().split()))
cats = [0] + list(map(int,input().split()))
tree = {}
for i in range(1, n + 1):
    tree[i] = []
for i in range(n-1):
    v1, v2 = list(map(int,input().split()))
    if v1 < v2:
        tree[v1].append(v2)
    else:
        tree[v2].append(v1)

#print(tree)
#print(cats)

visited = set()

def dfs(visited, graph, node, streak = 0, broken = False):  #function for dfs
    if cats[node] == 1:
        streak += 1
        if streak > m:
            broken = True
    if cats[node] == 0:
        streak = 0
    if node not in visited:
#        print (node , streak, broken)
        visited.add(node)
        if tree[node] == [] and not broken:
            dfs.able += 1
#            print(dfs.able)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour, streak, broken)
dfs.able = 0

dfs(visited, tree, 1)
print(dfs.able, end = '')
