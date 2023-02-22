import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]

t = ni()
for _ in range(t):
    n = ni()
    # in the case of two, 3, 1

    if n == 2:
        print("3 1")
    else:
        if n % 2 == 0:
            arr = [i for i in range(n - n//2, n)]
            arr += [i for i in range(n+1, n + n // 2 + 1)]
            print(*arr)
        else:
            #center at n, sum will be n^2
            r = n - 1
            diff = r // 2
            arr = [i+2 for i in range(n - diff, n + diff + 1)]
            #print(arr)
            arr[0]-=1
            arr[-1] += 1
            arr[-2] += 1 # to get to n^2 + 2n + 1 <-
            #print(arr)
            print(*arr)
        
            