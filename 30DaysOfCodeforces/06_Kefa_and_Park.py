import sys
sys.setrecursionlimit(10**5)

import sys


def setupInputOutputSublime():
    import os

    if os.name == 'nt':
        sys.stdout = open("C:\\Temp\\output.txt", mode = 'w')
        sys.stdin = open("C:\\Temp\\input.txt", mode = 'r')
#setupInputOutputSublime()


itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#solution to https://codeforces.com/problemset/problem/580/C

n, m = list(map(int,input().split()))
cats = [0] + list(map(int,input().split()))
tree = {}
for i in range(1, n + 1):
    tree[i] = []
for i in range(n-1):
    v1, v2 = list(map(int,input().split()))
    tree[v1].append(v2)
    tree[v2].append(v1)
 
#print(tree)
#print(cats)
 
visited = {}

#recursive approach
def dfs(visited, graph, node, streak = 0, broken = False, parent = 1):  #function for dfs
    if cats[node] == 1:
        streak += 1
        if streak > m:
            broken = True
    if cats[node] == 0:
        streak = 0
    if node not in visited:
#        print (node , streak, broken)
        visited[node] = True
        if tree[node] == [parent] and not broken:
            dfs.able += 1
#            print(dfs.able)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour, streak, broken, node)
dfs.able = 0

visited = {} # List to keep track of visited nodes.
queue = []     #Initialize a queue'



#iterative approach
def bfs(visited, graph, node):
    visited[node] = True
    #(node, current streak, longest streak)
    if cats[node]:
        queue.append((node,1,1))
    else:
        queue.append((node,0,0))

    while queue:
        s = queue.pop(0)
#        print (s) 
        parent = s[0]

        for neighbour in graph[parent]:
            if neighbour not in visited:
                visited[neighbour] = True
                if cats[neighbour]:
                    n = (neighbour,s[1]+1, max(s[1]+1,s[2]))
                else:
                    n = (neighbour,0,s[2])
                queue.append(n)
                if len(graph[neighbour]) == 1 and graph[neighbour] == [parent]:
    #                print("leaf")
                    if n[2] <= m:
#                        print(n)
                        bfs.able+= 1
bfs.able = 0


bfs(visited, tree, 1)
print(bfs.able)
