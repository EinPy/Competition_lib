import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



class TwoSat:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(2*n)]
        self.rev_graph = [[] for _ in range(2*n)]
        self.visited = [False] * (2*n)
        self.scc = [None] * (2*n)
        self.stack = []
        self.time = 0

    def add_clause(self, x, y):
        # x or y. If x is true, ¬y must be false and vice-versa
        self.graph[x^1].append(y)
        self.graph[y^1].append(x)
        self.rev_graph[y].append(x^1)
        self.rev_graph[x].append(y^1)

    def dfs1(self, u):
        self.visited[u] = True
        for v in self.graph[u]:
            if not self.visited[v]:
                self.dfs1(v)
        self.stack.append(u)

    def dfs2(self, u, index):
        self.scc[u] = index
        for v in self.rev_graph[u]:
            if self.scc[v] is None:
                self.dfs2(v, index)

    def find_sccs(self):
        for i in range(2*self.n):
            if not self.visited[i]:
                self.dfs1(i)

        while self.stack:
            v = self.stack.pop()
            if self.scc[v] is None:
                self.dfs2(v, self.time)
                self.time += 1

    def is_satisfiable(self):
        self.find_sccs()
        for i in range(self.n):
            if self.scc[i*2] == self.scc[i*2+1]:
                return False
        return True
    
    def add_xor(self, x, y):
        # Adding XOR between x and y
        self.add_clause(x, y^1)  # x OR ¬y
        self.add_clause(x^1, y)  # ¬x OR y

# Example usage

def vec(p1, p2):
    return p2[0]-p1[0], p2[1] - p1[1]

def sign(x):
    if x < 0: return -1
    return 1 if x > 0 else 0

def cross(u, v):
    return u[0] * v[1] - u[1] * v[0]

# s1: (Point, Point)
# s2: (Point, Point)
# Point : (x, y)
# returns true if intersecting s1 & s2 shares at least 1 point.
def is_segment_intersection(s1, s2):
    u = vec(*s1)
    v = vec(*s2)
    p1, p2 = s1
    q1, q2 = s2
    d1 = cross(u, vec(p1, q1))
    d2 = cross(u, vec(p1, q2))
    d3 = cross(v, vec(q1, p1))
    d4 = cross(v, vec(q1, p2))
    if d1 * d2 * d3 * d4 == 0:
        return True
    return sign(d1) != sign(d2) and sign(d3) != sign(d4)



w, p = nl()
wlls = []
pp = [[] for _ in range(w)]
for _ in range(w):
    wlls.append(nl())
for i in range(p):
    n, x, y = nl()
    pp[n-1].append([x,y,i+1])
    


twosat = TwoSat(p)

        

# no pipes intersect with another pipe from same well?
# for each pipe check all itnersections with pipes from other wells. 
for i in range(w):
    sx, sy = wlls[i]
    #for all pipes starting at well i
    for xf, yf, idx in pp[i]:
        #line from
        seg1 = ((sx,sy),(xf, yf))
        for j in range(i+1, w): #check all pipes starting in all other wells
            xs2, ys2 = wlls[j]
            for xf2, yf2, k in pp[j]:
                seg2 = ((xs2, ys2), (xf2, yf2))
                if is_segment_intersection(seg1, seg2):
                    #print(idx,"xor", k)
                    twosat.add_xor(idx, k)
                    
if twosat.is_satisfiable():
    print("possible")
    #print(G.solution())
else:
    print("impossible")
    #print(G.solution())

# Add clauses here, for example:
# twosat.add_clause(1, 2)  # x1 or x2
# twosat.add_clause(3, 0)  # ¬x1 or x3



