import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [float(_) for _ in INP().split()]



n, k, p = nl()


# monoid needs to implement
# __add__, __mul__, __sub__, __div__ and isZ 
def gauss(A, b, monoid=None):
    def Z(v): return abs(v) < 1e-6 if not monoid else v.isZ()

    N = len(A[0])
    for i in range(N):
        try:
            m = next(j for j in range(i, N) if Z(A[j][i]) == False)
        except:
            return None #A is not independent!
        if i != m:
            A[i], A[m] = A[m], A[i]
            b[i], b[m] = b[m], b[i]
        for j in range(i+1, N):
            sub = A[j][i]/A[i][i]
            b[j] -= sub*b[i]
            for k in range(N):
                A[j][k] -= sub*A[i][k]

    for i in range(N-1, -1, -1):
        for j in range(N-1, i, -1):
            sub = A[i][j]/A[j][j]
            b[i] -= sub*b[j]
        b[i], A[i][i] = b[i]/A[i][i], A[i][i]/A[i][i]
    return b



# 0 0 0 0 0 0
"""
z = 0 0 0 0 0 0 
E(0 0 0 0 0 0) = 1 + p * E(0 0 0 0 0 1) + (1-p) E(0 0 0 0 0 0)

E(0 0 0 0 0 1) = 1 + p*E(0 0 0 0 1 1) + (1-p) * E(0 0 0 0 1 0)

E(0 0 0 0 1 1) = 1 + p * E(0 0 0 1 1 1) + (1-p) * E(0 0 0 1 1 0)

"""
#create every state


cur = ["0"*int(n)]
seen = {}
mapping = {cur[0] : 0}
curIdx = 1
A = []
b = []
while cur:
    nxt =[]
    #start on a state, create the two next state
    for s in cur:
        if s not in seen:
            seen[s] = True
            #can go to 
            s1 = s[1:] + "1"
            s0 = s[1:] + "0"
            sv = 1

            if s.count("1") >= k:
                sv = 0

            #equation becoms
            #E(s) = 1 + p * E(s1) +(1-p)*E(s0)
            #E(s) - p * E(s1) + (p-1) * E(s0) = 1

            id1 = -1
            
            if s1 in mapping:
                id1 = mapping[s1]
            else:
                id1 = curIdx
                mapping[s1] = id1
                curIdx += 1
            
            id0 = -1
            if s0 in mapping:
                id0 = mapping[s0]
            else:
                id0 = curIdx
                mapping[s0] = id0
                curIdx += 1
            
            coeff = [0] *  int(2 ** n)
            #this is equation if only three params coeff = [1, -p, p -1]
            if sv == 0:
                coeff[mapping[s]] = 1
            else:
                if s == s0:
                    coeff[mapping[s]] = (sv + (p-1)) 
                    coeff[mapping[s1]] = -p 
                elif s == s1:
                    coeff[mapping[s]] = (1-p) * sv
                    coeff[mapping[s0]] = (p - 1) 
                else:
                    coeff[mapping[s]] = 1 * sv
                    coeff[mapping[s1]] = -p 
                    coeff[mapping[s0]] = (p - 1)
            
            const = 1
            A.append(coeff)
            b.append(const)
            if s0 not in seen:
                nxt.append(s0)
            if s1 not in seen:
                nxt.append(s1)
            
    cur = nxt
    
#print(A)
# for l in A:
#     print(l)
# print(b)
# print(seen)
# print(mapping)
print(gauss(A, b)[0] - 1)
# t = [[1, 2, 3, 5],
#      [3, 4, 5, 8],
#      [7, 8, 7, 9],
#      [12,13, 15,0]]
# b = [4, 10, 11, 10]
# print(gauss(t, b))
        
    