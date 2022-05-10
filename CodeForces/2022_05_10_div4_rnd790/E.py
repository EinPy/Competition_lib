#To start code
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


#code


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    n = len(arr)
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
        # means x is present at mid
        else:
            return mid+1
        
        if mid > 0 and x <= arr[mid] and x > arr[mid-1]:
            return mid+1
        
        if mid < n-1 and x > arr[mid] and x <= arr[mid+1]:
            return mid + 2
 
        
        
    #print(mid)

    return -1





t = ni()
for case in range(t):
    n, q = nl()
    a = nl()
    a.sort(reverse=True)
    cands = [0 for _ in range(n)]
    cands[0] = a[0]
    
    for i in range(1,n):
        cands[i] = cands[i-1] + a[i]
    #print(cands)
    for quer in range(q):
        goal = ni()
        if cands[0] >= goal:
            print(1)
        elif cands[-1] >= goal and cands[-2] < goal:
            print(n)
        else:
            print(binary_search(cands,goal))
