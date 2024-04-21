import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    pass


n = ni()
students = {}
for _ in range(n):
    a = INP()
    if a not in students:
        students[a] = 0
m = ni()
for _ in range(m):
    l = INP().split()
    if len(l) > 1:
        for s in l[1:]:
            students[s] += 1

arr = []

for k in students.keys():
    arr.append((students[k], k))
arr.sort(reverse=True)
for a, b in arr:
    print(a, b)
        
    