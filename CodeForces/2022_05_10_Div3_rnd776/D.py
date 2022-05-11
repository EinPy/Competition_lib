import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


    
def solve(n, arr):
    #print(arr)
    
    steps = [0 for _ in range(n)]
    
    for i in range(n, 1, -1):
        pos = arr.index(i)
        if pos == i-1:
            steps[i-1] = 0
        else:
            steps[i-1] = pos + 1
            newA = arr[pos+1:i] + arr[:pos] + [arr[pos]] + arr[i:]
            arr = newA
        #print(i, arr)
            
    steps[0] = 0
    
    print(" ".join(list(map(str,steps))))
        

t = ni()
for case in range(t):
    n = ni()
    arr = nl()
    solve(n, arr)
    
    

        
        
        
        