import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



class FenwickTree: # zero indexed calls!
    def __init__(self, sz):
        self.data = [0]*(sz+1)
    def inc(self, i, delta):
        i += 1 # (to 1 indexing)
        while i < len(self.data):
            self.data[i] += delta
            i += i&-i # lowest oneBit
    def sum(self, i):
        i += 1 # (to 1 indexing)
        S = 0
        while i > 0:
            S += self.data[i]
            i -= i&-i
        return S
    def query(self, lo, hi):
        return self.sum(hi) - self.sum(lo)
    

n, quer = nl()
a = nl()
tree = FenwickTree(n+2)
for _ in range(quer):
    l, r = nl()
    tree.inc(l,1)
    tree.inc(r+1,-1)
#now we have a tree that jhas the amount of times each thing was added
#test
#print(a)
a.sort()
appeareances = []
for i in range(1,n+1):
    appeareances.append(tree.sum(i))
    
appeareances.sort()
tot = 0
for i in range(1,n+1):
    tot += appeareances[n-i] * a[n-i]

print(tot)
