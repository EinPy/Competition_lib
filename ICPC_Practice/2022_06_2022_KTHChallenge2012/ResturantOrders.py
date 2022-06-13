import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(t, it, m, q):
    #[possible, ways, ambiguous]
    big = max(q) + 1
    memo = [[0,{}] for _ in range(big)]
    #first iteration
    memo[0][0] = 1
    
    for i in range(big):
        if memo[i][0] > 0:
            #print(i)
            if memo[i][0] == 1:
                for j in range(t):
                    newI = i + it[j]
                    #print("new", newI)
                    newD = memo[i][1].copy()
                    if j+1 not in newD:
                        newD[j+1] = 1
                    else:
                        newD[j+1] += 1
                    #print(newD)
                    if newI < big:
                        if memo[newI][0] == 0:
                            memo[newI][0] += 1
                            memo[newI][1] = newD
                        else:
                            if memo[newI][1] == newD:
                                #print("happned")
                                continue
                            else:
                                memo[newI][0] += 1
                                #print("happned")
                                #print(memo)
            elif memo[i][0] > 1:
                for j in range(t):
                    newI = i + it[j]
                    if newI < big:
                        memo[newI][0] += 2
    #print(memo)
    #print(m)
    for i in range(m):
        if memo[q[i]][0] == 0:
            print("Impossible")
        elif memo[q[i]][0] == 1:
            lst = memo[q[i]][1].keys()
            arr =list(lst)
            arr.sort()
            out = []
            for c in arr:
                out+= [memo[q[i]][1][c]] * c
            print(' '.join(map(str,out)))
        else:
            print("Ambiguous")
            
        
    
t = ni()
it = nl()
m = ni()
q = nl()
solve(t, it, m, q)