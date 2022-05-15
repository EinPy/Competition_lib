import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(a, b, p, arr):
    arr = list(arr)
    #count backwards
    arr.pop()
    i = len(arr) -1
    #print(arr)
    while p >= 0:
        stop = arr[i]
        #print(stop)
        if stop == "A":
            p -= a
        else: 
            p -= b
        
        if p < 0:
            #print("NEG")
            return i + 2
        elif p == 0:
            #print(arr[i], stop)
            while  i > 0 and arr[i-1] == stop:
                i -= 1
            #print("0")
            return i + 1
        else:
            while i > 0 and arr[i] == stop:
                i -= 1
            if i == 0 and arr[i] == stop:
                return 1
    if i == 0 and p < 0:
        return i+2
    return i + 1

t = ni()
for case in range(t):
    a, b, p = nl()
    arr = INP()
    print(solve(a, b, p, arr))