import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)


def solve(s):


T = int(input())
for i in range(T):
    n = int(input())
    s = list(map(int,input().split()))
    solve(s)
    