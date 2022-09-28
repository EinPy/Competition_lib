from lib2to3.pytree import convert
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



m, n = nl()
monX = {}
monY = {}
cX = {}
cY = {}
church = {}
for _ in range(m):
    x, y = nl()
    if x not in monX:
        monX[x] = 1
    else:
        monX[x] += 1
    if y not in monY:
        monY[y] = 1
    else:
        monY[y] += 1
        
for _ in range(n):
    x, y = nl()
    church[(x,y)] = True
    if x in monX and monX[x] == 1:
        if y not in monY or (y in monY and monY[y] < 2):
            if x not in cX:
                cX[x] = 1
            else:
                cX[x] += 1
                
    if y in monY and monY[y] == 1:
        if x not in monX or (x in monX and monX[x] <2):
            if y not in cY:
                cY[y] = 1
            else:
                cY[y] += 1
            

maxX, maxY = 0, 0
iX, iY = 0, 0
for i in cX.keys():
    if cX[i] >= maxX:
        maxX = cX[i]
        iX = i
        
XX = []
for i in cX.keys():
    if cX[i] == maxX:
        XX.append(i)
        
for i in cY.keys():
    if cY[i] > maxY :
        maxY = cY[i]
        iY = i

YY = []
for i in cY.keys():
    if cY[i] == maxY:
        YY.append(i)
        
for x in XX:
    for y in YY:
        if (x,y) not in church:
            iX, iY = x, y



#print(monX, monY, cX, cY)
conversion = maxX + maxY
if (iX, iY) in church:
    conversion -= 1
print(iX, iY)
print(conversion)



