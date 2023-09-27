import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

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



n = ni()
k =  nl()
total = n
#compute fref array from right
arr = [1 for n in range(n)]
#print(arr)
T = FenwickTree(arr)



def bns(start, diff):
    l = start
    r = n-1
    #goal is total - T.query(mid, n-1) = diff
    #find the rightmost person
    ans = -1
    mid = 0
    while l <= r:
        mid = (l + r) // 2
        trail = T.query(mid, n-1)
        #print(l, r, mid, trail)
        if trail == diff:
            ans = mid
            l = mid + 1
        elif trail  > diff:
            l = mid + 1
        else:
            r = mid - 1
    return ans




#print(T.query(0,3))
tot = n
next = k[0]
curI = 0


# def printTree(tree):
#     for i in range(n):
#         #print(tree.query(i,i), end = " ")


while tot > 1:
    #print("tree:")
    #printTree( T)
    #print()
    step = k[curI]
    to_right = T.query(curI, n-1)
    #print("starting from", curI, "counting", step)
    if to_right < step:
        step -= to_right
        step = (step-1) % tot
        diff = tot - step
        #print("from0", step, diff)
        remI = bns(0, diff)
        #print("remove", remI)
        tot -= 1
        T.inc(remI, -1)
        right = T.query(remI, n-1)
        if  right == 0:
            curI = bns(0, tot)
        else:
        #    print("last")
            curI = bns(remI, right)
        #    print(curI)
    else:
        diff = to_right - step
        remI = bns(curI, diff)
        tot -= 1
        T.inc(remI, -1)
        right = T.query(remI, n-1)
        if right == 0:
            curI = bns(0, tot)
        else:
            curI = bns(remI,right)
            
# print("tree:")
# printTree(T)
# print()
print(curI+1)
