import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


#index 2i is true, 2i + 1 is false
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
    
    
m, c = nl()
#print(m, c)
size = 2*m
S = Sat(size)
#bride is always true
#print(2*m)
S.add_or(0,0)
S.add_xor(0,2*m)
#print(0,m)
for i in range(1,m):
    S.add_xor(2*i, 2*(i + m))
    #print(i, i + m)


for r in range(c):
    a,b = INP().split()
    #man
    l, r = int(a[:-1]), int(b[:-1])
    if a[-1] == "h":
        #man
        if b[-1] == "h":
            S.add_or(2*(l + m), 2*(r + m))
        #woman
        else:
            S.add_or(2*(l + m), 2*r)
            
    #woman
    else:
        #man
        if b[-1] == "h":
            S.add_or(2*l, 2*(r + m))
        #woman
        else:
            S.add_or(2*l, 2*r)

ans = S.is_sat()
arr = S.solution()
#print(arr)
if ans:
    for i in range(1,m):
        if arr[i]:
            print(f"{i}w", end = " ")
        else:
            print(f"{i}h", end = " ")
else:
    print("bad luck")