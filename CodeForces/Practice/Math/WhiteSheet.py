import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]




def i(x1, y1, x2, y2, xx1, yy1, xx2, yy2):
    xint = max(0, min(x2, xx2) - max(x1, xx1))
    yint = max(0, min(y2,yy2) - max(y1, yy1))
    return xint * yint

def intCord(x1, y1, x2, y2, xx1, yy1, xx2, yy2):
    #if they intersect
    if  min(x2, xx2) - max(x1, xx1) > 0 and min(y2,yy2) - max(y1, yy1) > 0:
        nx1, nx2 = max(x1, xx1),  min(x2, xx2)
        ny1, ny2 = max(y1, yy1), min(y2,yy2)
        return nx1, ny1, nx2, ny2
    else:
        return -1
    
wx1, wy1, wx2, wy2 = nl()
b1x1, b1y1, b1x2, b1y2 = nl()
b2x1, b2y1, b2x2, b2y2 = nl()

newT1 = intCord(wx1, wy1, wx2, wy2, b1x1, b1y1, b1x2, b1y2)
newT2 = intCord(wx1, wy1, wx2, wy2, b2x1, b2y1, b2x2, b2y2)
overlap = 0
if newT1 != -1 and newT2 != -1:
    a, b, c, d = newT1
    e, f, g, h = newT2
    overlap += i(a,b,c,d,e,f,g,h)

wb1 = i(wx1, wy1, wx2, wy2, b1x1, b1y1, b1x2, b1y2)
wb2 = i(wx1, wy1, wx2, wy2, b2x1, b2y1, b2x2, b2y2)


Aw = (wx2 - wx1) * (wy2 - wy1)
tot = Aw - (wb1 + wb2 - overlap)
if tot > 0:
    print("YES")
else:
    print("NO")