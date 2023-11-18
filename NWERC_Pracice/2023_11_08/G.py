import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



#inversions is for all indexes, how many elements after it that is smaller than it. 

# 2 1, has one inversion
# 2 3 1, has 2 inversions
# 3 2 1, has 3 inversions
#2 1 3, has 1 inversion

# Tested on: https://open.kattis.com/problems/froshweek
class FenwickTree: # zero indexed calls!
    # Give array or size!
    def __init__(self, blob):
        if type(blob) == int:
            self.sz = blob
            self.data = [0]*(blob+1)
        elif type(blob) == list:
            A = blob
            self.sz = len(A)
            self.data = [0]*(self.sz + 1)
            for i, a in enumerate(A):
                self.inc(i, a)
    # A[i] = v
    def assign(self, i, v):
        currV = self.query(i, i)
        self.inc(i, v - currV)
    # A[i] += delta
    # this method is ~3x faster than doing A[i] += delta
    def inc(self, i, delta):
        i += 1 # (to 1 indexing)
        while i <= self.sz:
            self.data[i] += delta
            i += i&-i # lowest oneBit
    # sum(A[:i+1])
    def sum(self, i):
        i += 1 # (to 1 indexing)
        S = 0
        while i > 0:
            S += self.data[i]
            i -= i&-i
        return S
    # return sum(A[lo:hi+1])
    def query(self, lo, hi):
        return self.sum(hi) - self.sum(lo-1)



def pp(T):
    for i in range(T.sz):
        print(T.query(i,i), end = " ")
    print()
    
db = False
def solve(a1, a2, a3,sz):
    arrs = [a1, a2, a3]
    #start permutations at 0
    for i in range(3):
        for j in range(sz):
            arrs[i][j] -= 1
    
    #find inverions of all combinations, if invalid there will be 2 inverions, else 0
    #1 and 2
    #1 and 3
    #2 and 3
    #inversions are reversible, inversion of a to b = inversion b to a
    
    #need to keep track of where to find a_i, map pos[a_i] = i
    p1, p2, p3 = [0] * sz, [0] * sz, [0] * sz
    poss = [p1, p2, p3]
    for i in range(3):
        for j in range(sz):
            if db: print(i, j, arrs[i][j])
            poss[i][arrs[i][j]] = j
            
    if db: print(poss)
    if db: print(p1, p2, p3)
    
    T12 = FenwickTree([0] *sz)
    T13 = FenwickTree([0] * sz)
    T23 = FenwickTree([0] * sz)
    #count inversions between 1 and two
    inv = 0
    #a1 and a2
    for num in a1:
        #fill in num in 2, check if it comes before some num in 2, in that case, it is not in same order
        T12.inc(p2[num], 1)
        if p2[num] != sz- 1:
            inv += T12.query(p2[num] + 1, sz-1)
        T13.inc(p3[num], 1)
        if p3[num] != sz-1:
            inv += T13.query(p3[num] +1, sz-1)
    #a2 and a3
    for num in a2:
        T23.inc(p3[num], 1)
        if p3[num] != sz- 1:
            inv += T23.query(p3[num]+1,sz-1)

    #a1 and a3
    #inv is 2x the pairs that were ordered wrong
    #total amount of pairs is n*(n-1) / 2
    print(int(sz * (sz-1) / 2 - inv/2))

n = ni()
a1, a2, a3 = nl(), nl(), nl()

solve(a1, a2, a3, n)
        

        

