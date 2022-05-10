#To start code
import sys
from collections import *
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]


#code







def solve(n,k,a):
    a.sort()

    count = 1
    curNum = a[0]
    l, r = 0,1
    streak = 0
    biggestDiff = 0
    leftN, rightN = -1, -1 
    while r < n:
        while r < n and count < k:
            if a[r] == curNum:
                count += 1
                r += 1
            else: 
                if streak >= 2:
                    if a[r-1] - a[l] >= biggestDiff:
                        leftN = a[l]
                        rightN = a[r-1]
                        biggestDiff = a[r-1] - a[l]
                #reset
                l = r
                r += 1
                if r < n:
                    curNum = a[r]
                streak = 0
                count = 1
            #print(l,r)


        if count >= k:
            streak += 1
            if streak >= 2:
                if a[r-1] - a[l] >= biggestDiff:
                    leftN = a[l]
                    rightN = a[r-1]
                    biggestDiff = a[r-1] - a[l]
            while r < n and a[r] == curNum:
                r += 1
            
            if r < n:
                if a[r] != curNum + 1:
                    l = r
                    streak = 0
                curNum = a[r]
            count = 0
            
    if rightN == -1 or leftN == -1:
        return -1
    return f"{leftN} {rightN}"


t = ni()
for case in range(t):
    n, k = nl()
    a = nl()
    print(solve(n,k,a))