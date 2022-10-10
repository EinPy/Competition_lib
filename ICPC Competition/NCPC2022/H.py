import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    pass


t = ni()

h = nl()
m = 0

left = [0]*t
right = [0]*t
 
left[0]=10**18
right[t-1]=10**18

for i in range(1,t):
    if h[i]>=h[i-1]:
        left[i] = min(left[i-1],h[i-1])
    else:
        left[i] = 10**18
    
    if h[t-i-1] >= h[t-i]:
        right[t-i-1] = min(right[t-i],h[t-i])
    else:
        right[t-i-1] = 10**18

for i in range(t):
    temp = min(h[i]-left[i],h[i]-right[i])
    m = max(m,temp)

print(m)