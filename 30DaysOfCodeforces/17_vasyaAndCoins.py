import sys
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#code


def solve(a,b):
    if a:
        return a + b*2 + 1
    else:
        return 1

    
T = int(input())
for case in range(T):
    a, b = list(map(int,input().split()))
    print(solve(a,b))