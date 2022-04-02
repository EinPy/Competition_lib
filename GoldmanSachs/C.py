import string
import sys
import math
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)



def solve(cords):
    pass


def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])^2 + (p1[1] - p2[1])^2)

N = int(input())
cords = {}
cL = []
for i in range(N):
    x, y = (list(map(int,input().split())))
    cords[(x,y)] = True
    cL.append((x,y))
    
dists = [[] for _ in range(math.ceil(math.sqrt(2 * 20000*20000*2)))]
for p1 in range(len(cL)):
    for p2 in range(p1 + 1, len(cL)):
        d = distance(cL[p1],cL[p2])
        dists[d].append(math.ceil(d))




print(cords)
solve(cords)
