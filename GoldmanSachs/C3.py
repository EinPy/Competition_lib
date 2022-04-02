import string
import sys
import math
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)



def distSq(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1] - p2[1])**2

def squareChek(p1, p2, p3, p4):
    d2 = distSq(p1, p2) # from p1 to p2
    d3 = distSq(p1, p3) # from p1 to p3
    d4 = distSq(p1, p4) # from p1 to p4
    
    if d2 == d3 and 2 * d2 == d4 and \
                    2 * distSq(p2, p4) == distSq(p2, p3):
        return True
 
    # The below two cases are similar to above case
    if d3 == d4 and 2 * d3 == d2 and \
                    2 * distSq(p3, p2) == distSq(p3, p4):
        return True
 
    if d2 == d4 and 2 * d2 == d3 and \
                    2 * distSq(p2, p3) == distSq(p2, p4):
        return True
 
    return False

def solve(cL, dict):
    #counting between I and J
    sqrs = 0
    used = {}
    for i in range(len(cL)):
        for j in range(i + 1, len(cL)):
            x1, y1 = cL[i]
            x2, y2 = cL[j]
            new1 = ((x1 + x2 + y2 -y1)/2, (y1+y2+x1 - x2)/2)
            new2 = (((x1 + x2 + y1 -y2)/2, (y1+y2+x2 - x1)/2))
            if new1 in cords and new2 in cords:
                pnts = (cL[i],cL[j],new1, new2)
                hash = tuple(sorted(pnts))
                if hash not in used:
                    sqrs += 1
                    used[hash] = True
    print(sqrs)

N = int(input())
cords = {}
cL = []
for i in range(N):
    x, y = (list(map(int,input().split())))
    cords[(x,y)] = True
    cL.append((x,y))
    
#print(cords)
#print(distance((1,1),(3,3)))
#print(dists)
solve(cL, cords)
