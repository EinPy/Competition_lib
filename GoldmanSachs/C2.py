import string
import sys
import math
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)


def squareChek(a, b, c, d):
    dX1=  (a[0]-b[0])
    dY1 = (a[1]-b[1])
    dX2 =  c[0]-d[0]
    dY2 = (c[1]-d[1])
    if dX1 == dX2 and dY1 == dY2:
        return False
    
    if abs(dX1) + abs(dY1) == abs(dX2) + abs(dY2) and len((a,b,c,d)) == len(set((a,b,c,d))):
        return True
    return False

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2)

def solve(cL, dists):
    #counting between I and J
    used = {}
    sqrs = 0
    for p1 in range(len(cL)):
        for p2 in range(p1 + 1, len(cL)):
                dst = distance(cL[p1], cL[p2])
                for el in dists[math.ceil(dst)]:
                    tst = [cL[p1],cL[p2], el[0], el[1]]
                    tst.sort()
                    check = tuple(tst)
                    if squareChek(cL[p1],cL[p2], el[0], el[1]) and check not in used:
                        print(check)
                        sqrs+= 1
                        usd = [cL[p1],cL[p2], el[0], el[1]]
                        usd.sort()
                        t = tuple(usd)
                        used[t] = True
                for el in dists[math.floor(dst)]:
                    tst = [cL[p1],cL[p2], el[0], el[1]]
                    tst.sort()
                    check = tuple(tst)
                    if squareChek(cL[p1],cL[p2], el[0], el[1]) and check not in used:
                        print(check)
                        sqrs+= 1
                        usd = [cL[p1],cL[p2], el[0], el[1]]
                        usd.sort()
                        t = tuple(usd)
                        used[t] = True
    print(sqrs)
    #print(used)

N = int(input())
cords = {}
cL = []
for i in range(N):
    x, y = (list(map(int,input().split())))
    cords[(x,y)] = True
    cL.append((x,y))
    
dists = {}
for p1 in range(len(cL)):
    for p2 in range(len(cL)):
        d1 = math.ceil(distance(cL[p1],cL[p2]))
        d2 = math.floor(distance(cL[p1],cL[p2]))
        if d1 != 0:
            if d1 not in dists:
                dists[d1] = []
            if (cL[p1],cL[p2]) not in dists[d1]:
                dists[d1].append((cL[p1],cL[p2]))
        if d2 != 0:
            if d2 not in dists:
                dists[d2] = []
            if (cL[p1],cL[p2]) not in dists[d2]:
                dists[d2].append((cL[p1],cL[p2]))

#print(cords)
#print(distance((1,1),(3,3)))
#print(dists)
solve(cL, dists)
