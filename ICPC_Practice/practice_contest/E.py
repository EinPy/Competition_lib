import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    pass


N , K = nl()
arr = [int(_) - 1 for _ in INP().split()]

groups = []
seen = {}
curG = 0 
print(arr)
for i in range(N):
    if i not in seen and arr[i] not in seen:
        groups.append([i, arr[i]])
        seen[i] = curG
        seen[arr[i]] = curG
        curG += 1
    elif i in seen and arr[i] not in seen:
        groups[seen[i]].append(arr[i])
        seen[arr[i]] = seen[i]
    elif arr[i] in seen and i not in seen:
        groups[seen[arr[i]]].append(i)
        seen[i] = seen[arr[i]]
        
        
print(groups)
print(seen)

#sort all cycles in a possible way
tot_order = [-1 for _ in range(N)]
for cyc in groups:
    steps = K % len(cyc)
    #set first in group to be first in order, does not matter        
    order = [-1 for _ in range(len(cyc))]
    order[0] = cyc[0]
    curN = cyc[0]
    curI = 0
    for i in cyc:
        to = arr[curN]
        newIdx = (curI + steps) % len(cyc)
        order[newIdx] = to
        curI = newIdx
        curN = arr[curN] 
        
    for i in range(len(order)):
        tot_order[order[i]] = order[(i+1) % len(order)] + 1
        
print(" ".join(map(str, tot_order)))
        

    
    