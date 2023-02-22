import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def DFS(graph, start, end, visited, path):
    # Mark the current node as visited
    visited[start[0]][start[1]] = True
    # Add the current node to the path
    path.append(start)

    # Check if the current node is the end node
    if start == end:
        # If the current node is the end node, return the path
        return path

    # Get the number of rows and columns in the graph
    rows = len(graph)
    cols = len(graph[0])

    # Check if the current node has any neighbors
    # A neighbor is a node that is adjacent to the current node and is a valid road (i.e. has value "B")
    neighbors = []
    if start[0] > 0 and graph[start[0] - 1][start[1]] == "B" and not visited[start[0] - 1][start[1]]:
        neighbors.append((start[0] - 1, start[1]))
    if start[0] < rows - 1 and graph[start[0] + 1][start[1]] == "B" and not visited[start[0] + 1][start[1]]:
        neighbors.append((start[0] + 1, start[1]))
    if start[1] > 0 and graph[start[0]][start[1] - 1] == "B" and not visited[start[0]][start[1] - 1]:
        neighbors.append((start[0], start[1] - 1))
    if start[1] < cols - 1 and graph[start[0]][start[1] + 1] == "B" and not visited[start[0]][start[1] + 1]:
        neighbors.append((start[0], start[1] + 1))

    # If the current node has any neighbors, visit each neighbor and search for the end node
    for neighbor in neighbors:
        result = DFS(graph, neighbor, end, visited, path)
        # If the end node is found, return the path
        if result:
            return result

    # If the end node is not found, remove the current node from the path and return False
    path.pop()
    return False

# Define the start and end nodes
start = (0, 0)
end = (2, 2)

# Create a matrix to track which nodes have been visited
visited = [[False for _ in range(len(graph[0]))] for _ in range(len(graph))]

# Perform DFS to search for the end node
result = DFS(graph, start, end, visited, [])

# Check if a path was found
if result:
    print




