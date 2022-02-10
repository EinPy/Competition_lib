import sys
sys.setrecursionlimit(10**5)

import sys


def setupInputOutputSublime():
    import os

    if os.name == 'nt':
        sys.stdout = open("C:\\Temp\\output.txt", mode = 'w')
        sys.stdin = open("C:\\Temp\\input.txt", mode = 'r')
setupInputOutputSublime()


itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#https://codeforces.com/problemset/problem/455/A

n = int(input)
a = list(map(int,input().split()))

# not for today, look at this https://bruceoutdoors.wordpress.com/2015/11/08/445a-boredom-codeforces-tutorial/
dp = [0 for _ in range(n) + 1]
def solve():
    if len(a) == 0:
        return

