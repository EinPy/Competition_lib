import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


import heapq as h

db = False
def solve(arr, m):
    #print(arr)
    q = []
    h.heapify(q)
    act = 0
    save = 0
    
    #use heap? 
    #greedy approach, always grab the one that terminates first?
    for s, d in arr:
        if act == 0:
            #start computer, and add it to heap, use earliset termination if it has started
            h.heappush(q, s + d)
            act += 1
            if db: print("add computer starting at",s+d )
        else:
            while act and q[0] + m < s: #remove unusable
                a = h.heappop(q)
                if db: print("remove unusable starting at", a)
                act -= 1
            if db: print("next available is", q[0], q[0] + m)
            if act and q[0] <= s and q[0] + m >= s: #use active
                a = h.heappop(q)
                if db: print("use active starting att", a)
                h.heappush(q, s + d)
                save += 1
            else: #start new
                h.heappush(q, s + d)
                act += 1
    print(save)
                
    
    
    
    
n, m = nl()
arr = []
for _ in range(n):
    arr.append(nl())
arr.sort()
#print(arr)
solve(arr, m)