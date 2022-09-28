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
    
    
n, q = nl()
arr = nl()
tree = FenwickTree(n)
for i in range(n):
    tree.inc(i, arr[i])
    
for _ in range(q):
    a, b, c = nl()
    if a == 1:
        cur = tree.query(b-2, b-1)
        diff = c - cur
        tree.inc(b-1, diff)
    if a == 2:
        print(tree.query(b-2, c-1))
        
   #for i in range(n):
        #print(tree.query(i-1, i), end = ' ')
    #print()