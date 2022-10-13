from operator import le
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

import math

n = ni()
d = {}
p = []
for _ in range(n):
    a, b = nl()
    if a not in d:
        d[a] = [b]
    else:
        d[a].append(b)
    p.append((a,b))



# A Python3 program to check if a given point 
# lies inside a given polygon
# Refer https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
# for explanation of functions onSegment(),
# orientation() and doIntersect() 
 
# Define Infinite (Using INT_MAX 
# caused overflow problems)
INT_MAX = 10000
 
# Given three collinear points p, q, r, 
# the function checks if point q lies
# on line segment 'pr'
def onSegment(p:tuple, q:tuple, r:tuple) -> bool:
     
    if ((q[0] <= max(p[0], r[0])) &
        (q[0] >= min(p[0], r[0])) &
        (q[1] <= max(p[1], r[1])) &
        (q[1] >= min(p[1], r[1]))):
        return True
         
    return False
 
# To find orientation of ordered triplet (p, q, r).
# The function returns following values
# 0 --> p, q and r are collinear
# 1 --> Clockwise
# 2 --> Counterclockwise
def orientation(p:tuple, q:tuple, r:tuple) -> int:
     
    val = (((q[1] - p[1]) *
            (r[0] - q[0])) -
           ((q[0] - p[0]) *
            (r[1] - q[1])))
            
    if val == 0:
        return 0
    if val > 0:
        return 1 # Collinear
    else:
        return 2 # Clock or counterclock
 
def doIntersect(p1, q1, p2, q2):
     
    # Find the four orientations needed for 
    # general and special cases
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
 
    # General case
    if (o1 != o2) and (o3 != o4):
        return True
     
    # Special Cases
    # p1, q1 and p2 are collinear and
    # p2 lies on segment p1q1
    if (o1 == 0) and (onSegment(p1, p2, q1)):
        return True
 
    # p1, q1 and p2 are collinear and
    # q2 lies on segment p1q1
    if (o2 == 0) and (onSegment(p1, q2, q1)):
        return True
 
    # p2, q2 and p1 are collinear and
    # p1 lies on segment p2q2
    if (o3 == 0) and (onSegment(p2, p1, q2)):
        return True
 
    # p2, q2 and q1 are collinear and
    # q1 lies on segment p2q2
    if (o4 == 0) and (onSegment(p2, q1, q2)):
        return True
 
    return False
 
# Returns true if the point p lies 
# inside the polygon[] with n vertices
def is_inside_polygon(points:list, p:tuple) -> bool:
     
    n = len(points)
     
    # There must be at least 3 vertices
    # in polygon
    if n < 3:
        return False
         
    # Create a point for line segment
    # from p to infinite
    extreme = (INT_MAX, p[1])
     
    # To count number of points in polygon
      # whose y-coordinate is equal to
      # y-coordinate of the point
    decrease = 0
    count = i = 0
     
    while True:
        next = (i + 1) % n
         
        if(points[i][1] == p[1]):
            decrease += 1
         
        # Check if the line segment from 'p' to 
        # 'extreme' intersects with the line 
        # segment from 'polygon[i]' to 'polygon[next]'
        if (doIntersect(points[i],
                        points[next],
                        p, extreme)):
                             
            # If the point 'p' is collinear with line 
            # segment 'i-next', then check if it lies 
            # on segment. If it lies, return true, otherwise false
            if orientation(points[i], p,
                           points[next]) == 0:
                return onSegment(points[i], p,
                                 points[next])
                                  
            count += 1
             
        i = next
         
        if (i == 0):
            break
             
    # Reduce the count by decrease amount
      # as these points would have been added twice
    count -= decrease
     
    # Return true if count is odd, false otherwise
    return (count % 2 == 1)
 
    


def inside(n, r, x, y):
    radPV = 2* math.pi / n
    corners = [(r, 0)]
    print( radPV, math.degrees(radPV))
    for v in range(1,n):
        #print(math.degrees(v * radPV))
        c1 = r * math.cos(v * radPV)
        c2 = r * math.sin(v * radPV)
        corners.append((c1,c2))
    print("out",n, r, x, y, corners)
    
    if is_inside_polygon(points = corners, p = (x, y)):
        return True
    else:
        print("not inside", x, y, corners)
        return False
    

def allInsideCheck(n,r):
    for x, y in p:
        if not inside(n,r,x,y):
            print("something not inside")
            return False
    #print("all inside")
    return True

def outsideCheck(n,r):
    for x, y in p:
        if inside(n,r,x,y):
            return False
    return True

#Binary search for lower bound
def lower_bound(n):
    l, r, mid = 0, 3*1e6, 0
    ans = -1
    while abs(l - r) > 2e-6 and l < r:
        mid = (l + r) / 2
        print(mid)
        if allInsideCheck(n,mid):
            print("all inside")
            ans = mid
            r = mid- 0.00000001
        else:
            l = mid + 0.00000001    
    return ans

def higher_bound(n):
    l, r, mid = 0, 2*1e6, 0
    ans = -1
    while abs(l - r) > 2e-6 and l < r:
        mid = (l + r) / 2
        if outsideCheck(n,mid):
            ans = mid
            l = mid + 0.00000001
        else:
            r = mid- 0.00000001
    return ans


def run():
    best = 1e18
    bestN = 0
    i = 3
    r_o = lower_bound(i)
    r_i = higher_bound(i)
    rad = math.pi * (i-2)
    radPV = rad / i
    A_o = (1/2) * r_o * r_o * math.sin(radPV) * i
    A_i = (1/2) * r_i * r_i * math.sin(radPV) * i
    print(r_o, r_i)
    if A_o - A_i < best:
        best = A_o - A_i
        bestN = i
    print(bestN, best)
            
        
inside(4,5,1,1)
print(str(10**(-6)))
run()
print(is_inside_polygon([ (-10,10),(-10, -10), (10,0)], (10,10)))