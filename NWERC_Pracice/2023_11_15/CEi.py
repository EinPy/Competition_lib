import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



w, p = nl()
wlls = []
pp = [[] for _ in range(w)]
for _ in range(w):
    wlls.append(nl())
for i in range(p):
    n, x, y = nl()
    pp[n-1].append([x,y,i])
    
#index 2i is true, 2i + 1 is false

adj, adjT = [[] for _ in range(2*p)], [[] for _ in range(2*p)]
used = [False for _ in range(2*p)]

order, comp = [], [-1 for _ in range(2*p)]
assignment = []

#for a node k index tk is true and 2k + 1 is false
#na and nb are booleans signaling whether
#a and b are to be negated, if they are negated
#uses xor operator to add 1. 
#add edge between (A OR B)
def addEdge(a, na, b, nb):
    #print(a,b)
    #2a will always be even, XOR (^) adds one if it is supposed to be False
    a = 2* a ^ na
    b = 2* b ^ nb
    #the negation is simply the opposite
    neg_a = a ^1 
    neg_b = b^1
    #not a -> b
    #not b -> a
    adj[neg_a].append(b)
    adj[neg_b].append(a)
    #for the transpose graph
    adjT[b].append(neg_a)
    adjT[a].append(neg_b)

def addXorEdge(a, b):
    # Add edges for (a OR b) and (¬a OR ¬b)
    addEdge(a, False, b, False)  # a -> ¬b (equivalent to ¬a OR b)
    addEdge(b, False, a, False)  # b -> ¬a (equivalent to ¬b OR a)
    addEdge(a, True, b, True)    # ¬a -> b (equivalent to a OR ¬b)
    addEdge(b, True, a, True)    # ¬b -> a (equivalent to b OR ¬a)


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
                    addXorEdge(idx,  k)

       
def dfs1(v):
    used[v] = True
    for u in adj[v]:
        if not used[u]:
            dfs1(u)    
    order.append(v)

def dfs2(v, cl): 
    comp[v] = cl
    for u in adjT[v]:
        if comp[u] == -1:
            dfs2(u,cl)

def solve_2SAT():
    #first dfs
    for i in range(2 * p):
        if not used[i]:
            dfs1(i)

    j = 0 #to keep track of which strongly connected component
    for i in range(2*p):
        #reversing the order from the dfs1 to 
        #visit the graph in reverse topological order
        v = order[2*p - i - 1]
        if comp[v] == -1:
            j += 1
            dfs2(v, j)
    
    #Finding a possible configuration
    assignment = [False for _ in range(p)]
    for i in range(0,2*p, 2):
        if comp[i] == comp[i+1]:
            return 0
        assignment[i//2] = comp[i] > comp[i+1]
        
    return 1

if(solve_2SAT()):
    print("possible")
else:
    print("impossible")