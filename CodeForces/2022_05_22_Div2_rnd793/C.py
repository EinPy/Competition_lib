import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]



def solve(n,a):
    cnt = Counter(a)
    inc = set(a)

    #print(inc)
    doubles = 0
    for num in inc:
        #print(num, cnt[num])
        if cnt[num] >= 2:
            #print("this")
            doubles += 1
    #print(doubles)
    if doubles == len(inc):
        print(doubles)
    else:
        sin = len(inc)
        #shared element
        sin -= 1
        print((doubles + 1) + (sin- doubles) // 2)



t = ni()
for case in range(t):
    n = ni()
    a = nl()
    solve(n,a)