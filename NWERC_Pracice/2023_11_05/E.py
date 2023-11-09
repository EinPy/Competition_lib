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

    # for indexing - nice to have but not required
    def __fixslice__(self, k):
        return slice(k.start or 0, self.sz if k.stop == None else k.stop)
    def __setitem__(self, i, v):
        self.assign(i, v)
    def __getitem__(self, k):
        if type(k) == slice:
            k = self.__fixslice__(k)
            return self.query(k.start, k.stop - 1)
        elif type(k) == int:
            return self.query(k, k)


def r(i,n): return (i + 1) % n
def l(i, n): return i -1 if i-1 >= 0 else n-1
    
def solve(k,n):
    #find shortest rotation, complexity N Log(N)
    B = [1 for _ in range(n)]
    #print(B, len(k))
    T = FenwickTree(B)
    cur = 0
    ops = 0
    lstep, rstep = 0,0
    for i in range(len(k)):
        # print("at ", cur, " remove ", k[i])
        # printTree(T)
        rstep = 0
        lstep = 0
        if cur == k[i]:
            ops += 1
            #print("cost was 1")
            T.assign(cur, 0)
            cur = r(cur,n)
        else:
            lb = max(cur - 1, 0)
            rb = min(n-1, cur+1)
            if k[i] < cur:
                #left
                lstep = T.query(k[i], lb)
                #right
                if rb != n-1:
                    rstep += T.query(rb, n-1)
                rstep += + T.query(0,k[i])
            else:
                #left
                if lb != 0:
                    lstep += T.query(0, lb)
                lstep = T.query(k[i], n-1)
                #right
                rstep = T.query(rb, k[i])

            if T.query(cur, cur) == 0:
                rstep -= 1
            # if lstep < rstep:
            #     print("went left")
            # elif lstep > rstep:
            #     print("went right")
            # elif lstep == rstep:
            #     print("tie")
            # print("cost was", min(rstep, lstep) + 1)
            ops += min(rstep, lstep) + 1
            
            cur = k[i]
            T.assign(cur, 0)
            cur = r(cur,n)
        #print("after removal")
        #printTree(T)
        #print(T.query(0,0),T.query(1,1),T.query(2,2))
            
    
            
    #print(T[:], T[:1], T[:2], T[:3])
    
    print(ops)
    
    return 0

def printTree(T):
    #print(T.sz)
    for i in range(T.sz):
        print(T.query(i, i), end = " ")
    print()
    
for i in range(28):
    t = ni()
    k = [0 for _ in range(t)]
    for i in range(t):
        k[i] = ni() - 1

    solve(k,t)

# Test = [1, 1, 1, 1, 1]
# TT = FenwickTree(Test)
# printTree(TT)
# print(TT.query(0,4))
# print(TT.query(0,-1))
# TT.inc(0, -1)
# printTree(TT)
