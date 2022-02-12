import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)


def solve(a):
    return max(a) - min(a)
    

T = int(input())
for i in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    print(solve(a))
    