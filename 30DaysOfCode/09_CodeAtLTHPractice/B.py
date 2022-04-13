import sys

def setupInputOutputSublime():
    import os

    if os.name == 'nt':
        sys.stdout = open("D:\\Temp\\output.txt", mode = 'w')
        sys.stdin = open("D:\\Temp\\input.txt", mode = 'r')
setupInputOutputSublime()
from math import sqrt

itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#code starts here
from collections import deque

#time limit exceeded

def bfs(graph,queue, visited):
    #(node, current streak, longest streak)
    maxDist= 0
    yM = len(graph)-1
    xM = len(graph[0])-1
    queue = deque(queue)

    while queue:
        (y, x), d = queue.popleft()
        if graph[y][x]== 1:
            maxDist = max(maxDist,d)

        N = []
        if y < yM:
            N.append((y + 1, x))
        if y > 0:
            N.append((y - 1, x))
        if x < xM:
            N.append((y, x +1))
        if x > 0:
            N.append((y, x-1))
        visited[y][x] = True

        for neigh in N:
            if not visited[neigh[0]][neigh[1]]:
                visited[neigh[0]][neigh[1]] = True
                n = (neigh, d + 1)
                queue.append(n)
    print(maxDist)


n = int(input())
adjMax = []
queue = []
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    line = str(input())
    newL = []
    for j in range(n):
        if line[j] == '3':
            queue.append(((i,j),0))
        newL.append(int(line[j]))
    adjMax.append(newL)

bfs(adjMax, queue, visited)
