import sys
from collections import *

from fractions import Fraction
import math

import matplotlib.pyplot as plt

sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [Fraction(_) for _ in INP().split()]





# Distance between two points
def dist(p, q):
    return math.hypot(p[0]-q[0], p[1] - q[1])

def vec(p1, p2):
    return p2[0]-p1[0], p2[1] - p1[1]

def sign(x):
    if x < 0: return -1
    return 1 if x > 0 else 0

def cross(u, v):
    return u[0] * v[1] - u[1] * v[0]

def on_segment(p, q, r):
    """Check if point q lies on line segment 'pr'"""
    if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and 
        q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
        return True
    return False

def is_segment_intersection(s1, s2):
    u = vec(*s1)
    v = vec(*s2)
    p1, p2 = s1
    q1, q2 = s2

    # Calculate cross products
    d1 = cross(u, vec(p1, q1))
    d2 = cross(u, vec(p1, q2))
    d3 = cross(v, vec(q1, p1))
    d4 = cross(v, vec(q1, p2))

    # Check general case
    if d1 != 0 or d2 != 0 or d3 != 0 or d4 != 0:
        return sign(d1) != sign(d2) and sign(d3) != sign(d4)

    # Check collinear case
    return (on_segment(p1, q1, p2) or on_segment(p1, q2, p2) or
            on_segment(q1, p1, q2) or on_segment(q1, p2, q2))
    
# Converts two points to a line (a, b, c),
# ax + by + c = 0
# if p == q, a = b = c = 0
def pts2line(p, q):
    return (-q[1] + p[1],
          q[0] - p[0],
          p[0]*q[1] - p[1]*q[0])
    
# projects a point on a line
def project(l, p):
    a, b, c = l
    return ((b*(b*p[0] - a*p[1]) - a*c)/(a*a + b*b),
        (a*(a*p[1] - b*p[0]) - b*c)/(a*a + b*b))
    
def has_point_inside(pts, lines):
    #project points onto line, if they came closer to origo, they are outide, if they moved farther away, they are inside
    for p in pts:
        dst = dist((0,0), p)
        for a, b in lines:
            l = pts2line(a, b)
            p2 = project(l, p)
            if dist((0,0), p2) > dst: #moved further away
                return True
    return False
            
def has_point_outside(pts, lines):  
    for p in pts:
        dst = dist((0,0), p)
        for a, b in lines:
            l = pts2line(a, b)
            p2 = project(l,p)
            if dist((0,0), p2) < dst: #moved closer
                return True
            
    return False

# def ok(pts, lines, shouldBeOutside):
#     for p in pts:
#         intsersects = False
#         for a, b in lines:
#             if is_segment_intersection(((0,0),p),(a, b)):
#                 intsersects = True
#         if shouldBeOutside:
#             if not intsersects:
#                 return False
#         if not shouldBeOutside:
#             if intsersects:
#                 return False
#     return True

# def hasIntersection(pts, lines):
#     for p in pts:
#         intsersects = False
#         for a, b in lines:
#             if is_segment_intersection(((0,0),p),(a, b)):
#                 intsersects = True
#         if not intsersects:
#             return False
#     return True

# def hasNoIntersection(pts, lines):
#     for p in pts:
#         intsersects = True
#         for a, b in lines:
#             if is_segment_intersection(((0,0),p),(a, b)):
#                 intsersects = False
#         if intsersects:
#             return False
#     return True

def hasPointInside(pts, lines):
    for p in pts:
        if p[0] == 0 and p[1] == 0:
            return True

        inside = True
        for l in lines:
            if is_segment_intersection(((0, 0), p), l):
                inside = False
        if inside:
            return True
    return False

def hasPointOutside(pts, lines):
    for p in pts:
        outside = False
        for l in lines:
            if is_segment_intersection(((0, 0), p), l):
                outside = True
        if outside:
            return True

    return False
    
            

def bns(pts, k):
    #print(pts)
    l, h = Fraction(0), Fraction(3 * 10 ** 6 + 5)
    mid = Fraction((l+h) / 2)
    ansi = 0
    #inner radius
    for _ in range(60):
        mid = (l+h) / 2
        lines = gen_lin_segs(mid, k)
        if hasPointInside(pts, lines):
            h = mid
        else:
            ansi = mid
            l = mid
        
    innerL = lines
    #outer radius
    l, h = Fraction(0), Fraction(3 * 10 ** 6 + 5)
    mid = Fraction((l+h) / 2)
    anso = 10**6+5
    #outer
    for _ in range(60):
        mid = (l+h) / 2
        lines = gen_lin_segs(mid, k)
        if  hasPointOutside(pts, lines):
            l = mid
        else:
            anso = mid
            h = mid
    outerL = lines
    #print(mid)
    #print(ansi, anso)
    #return (area_ratio_regular_polygons(k, ansi, anso))
    return ansi ** 2 / anso**2 , innerL, outerL
    

def gen_lin_segs(r, k):
    circ = Fraction(2 * math.pi)

    #binary serach over distance to inner corner
    cords = []
    theta = Fraction(circ / k)
    for seg in range(k):
        cords.append((Fraction(r * math.cos(theta * seg)), Fraction(r * math.sin(theta* seg))))
    lines = []
    for i in range(k-1):
        lines.append((cords[i], cords[i+1]))
    lines.append((cords[-1], cords[0]))
    
    return lines
    

def plooting(innL, outL, pts):
    for segment in innL:
        x_values = [segment[0][0], segment[1][0]]
        y_values = [segment[0][1], segment[1][1]]
        plt.plot(x_values, y_values, marker='o')
    for segment in outL:
        x_values = [segment[0][0], segment[1][0]]
        y_values = [segment[0][1], segment[1][1]]
        plt.plot(x_values, y_values, marker='o')
        
    x_coords = [p[0] for p in pts]
    y_coords = [p[1] for p in pts]

    # Create a scatter plot
    plt.scatter(x_coords, y_coords)

    # Setting plot features
    plt.title("Line Segments Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)



    # Show the plot
    plt.show()

def solve(pts):
    corners = [i for i in range(3, 9)]
    
    best = -1
    crn = 0
    innL = []
    outL = []
    for c_cnt in corners:
        A, iL, oL = bns(pts, c_cnt)
        if A > best:
            best = A
            crn = c_cnt
            innL = iL
            outL = oL
            
    plooting(innL, outL, pts)
        
    print(crn, "{:.10f}".format(float(best)))
    

n_points = ni()
pts =[]
for _ in range(n_points):
    x, y = nl()
    
    pts.append([Fraction(x), Fraction(y)])
    
    
solve(pts)
# pts = [(100, 100), (100, 100)]
# pts2 = [[-4, -1], [-4, 6], [-3, -6], [-3, 4], [0, -4], [2, -3], [2, 3], [5, 1], [7, 0]]
# lines = gen_lin_segs(100, 3)
# print(lines)
# print(hasPointInside(pts2, lines))
# print(hasPointOutside(pts2, lines))
# print(hasPointOutside(pts2, lines))

#import matplotlib.pyplot as plt
# line_segments = gen_lin_segs(10000, 8)
# # Plotting each line segment
# for segment in line_segments:
#     x_values = [segment[0][0], segment[1][0]]
#     y_values = [segment[0][1], segment[1][1]]
#     plt.plot(x_values, y_values, marker='o')

# # Setting plot features
# plt.title("Line Segments Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.grid(True)

# # Show the plot
# plt.show()