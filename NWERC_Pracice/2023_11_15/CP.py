import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

class Sat:
    def __init__(self, no_vars):
        self.size = no_vars*2
        self.no_vars = no_vars
        self.adj = [[] for _ in range(self.size)]
        self.back = [[] for _ in range(self.size)]
    def add_imply(self, i, j):
        self.adj[i].append(j)
        self.back[j].append(i)
    def add_or(self, i, j):
        self.add_imply(i^1, j)
        self.add_imply(j^1, i)
    def add_xor(self, i, j):
        self.add_or(i, j)
        self.add_or(i^1, j^1)
    def add_eq(self, i, j):
        self.add_xor(i, j^1)
    
    def dfs1(self, i):
        if i in self.marked: return
        self.marked.add(i)
        for j in self.adj[i]:
            self.dfs1(j)
        self.stack.append(i)

    def dfs2(self, i):
        if i in self.marked: return
        self.marked.add(i)
        for j in self.back[i]:
            self.dfs2(j)
        self.comp[i] = self.no_c

    def is_sat(self):
        self.marked = set()
        self.stack = []
        for i in range(self.size):
            self.dfs1(i)
        self.marked = set()
        self.no_c = 0
        self.comp = [0]*self.size
        while self.stack:
            i = self.stack.pop()
            if i not in self.marked:
                self.no_c += 1
                self.dfs2(i)
        for i in range(self.no_vars):
            if self.comp[i*2] == self.comp[i*2+1]:
                return False
        return True

    # assumes is_sat. 
    # If ¬xi is after xi in topological sort,
    # xi should be FALSE. It should be TRUE otherwise.
    # https://codeforces.com/blog/entry/16205
    def solution(self):
        V = []
        for i in range(self.no_vars):
            V.append(self.comp[i*2] > self.comp[i*2^1])
        return V

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



w, p = nl()
wlls = []
pp = [[] for _ in range(w)]
for _ in range(w):
    wlls.append(nl())
for i in range(p):
    n, x, y = nl()
    pp[n-1].append([x,y,i])
    


G = Sat(p+2)

        

# no pipes intersect with another pipe from same well?
# for each pipe check all itnersections with pipes from other wells. 
for i in range(w):
    sx, sy = wlls[i]
    #for all pipes starting at well i
    for xf, yf, idx in pp[i]:
        #line from
        seg1 = ((sx,sy),(xf, yf))
        for j in range(w): #check all pipes starting in all other wells
            if i != j:
                xs2, ys2 = wlls[j]
                for xf2, yf2, k in pp[j]:
                    seg2 = ((xs2, ys2), (xf2, yf2))
                    if is_segment_intersection(seg1, seg2):
                        #print(idx,"xor", k)
                        G.add_xor(idx*2, k*2)
                    
if G.is_sat():
    print("possible")
    #print(G.solution())
else:
    print("impossible")
    #print(G.solution())