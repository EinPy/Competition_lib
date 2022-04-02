import string
import sys
import math
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)


def solve(P):
    starts = [[0,True] for _ in range(len(P))]
  
    for i, pos in enumerate(P):
        if i == len(P)-1:
            alc, dist = pos
            for s in range(len(starts)):
                if s == 0 and starts[s][1] == True:
                    starts[s][0] += alc
                    if starts[s][0] - dist >= 0:
                        return s+1
                starts[s][0] += alc
                starts[s][0] -= dist
                if starts[s][0] <= 0:
                    starts[s][1] = False  
        else:   
            alc, dist = pos
            for s in range(i+1):
                starts[s][0] += alc
                starts[s][0] -= dist
                if starts[s][0] <= 0:
                    starts[s][1] = False
    
    for i in range(len(P)):
        alc, dist = P[i]
        if i == len(P) - 1:
            if starts[-1][1]:
                starts[-1][0] += alc
                if starts[-1][0] - dist >= 0:
                    return i+1
        else:
            if starts[i+1][1] == True:
                starts[i+1][0] += alc
                starts[i+1][0] -= dist
                if starts[i+1][0] >= 0:
                    return i+2
            for s in range(i, len(P)):
                starts[s][0] += alc
                starts[s][0] -= dist
                if starts[s][0] <= 0:
                    starts[s][1] = False
    return "impossible"
    

def takeIn():
    N = int(input())
    P = []
    for i in range(N):
        A, D= (list(map(int,input().split())))
        P.append([A,D])
        
    #print(cords)
    #print(distance((1,1),(3,3)))
    #print(dists)
    print(solve(P))

takeIn()