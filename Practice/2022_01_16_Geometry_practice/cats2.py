import sys
sys.setrecursionlimit(10**5)

itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)
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

dfs(visited, tree, 1)
print(dfs.able, end = '')
