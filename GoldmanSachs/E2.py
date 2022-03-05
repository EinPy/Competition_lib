import string
import sys
import math
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)


def solve(P):
    mostAlc = 0
    ind = 0
    cur = 0
    beenAbove = False
    
    for i, pos in enumerate(P):
        cur += pos[0]
        cur -= pos[1]
        if cur > mostAlc:
            if cur > 0:
                beenAbove = True
            mostAlc = cur
            ind = i
    if mostAlc >= 0 and beenAbove:
        return ind
    else:
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