import sys
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#code

def solve(n,arr):
    cost = 0
    for i in range(n-1):
        l = 1e9
        for p in range(i,n):
            if arr[p] < l:
                pos = p
                l = arr[p]
        cost += pos - i + 1
#        print(i, pos)
        mid = arr[i:pos+1]
        mid.reverse()
        arr = arr[:i] + mid + arr[pos+1:]
#        print(arr)
    return cost


T = int(input())
for case in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    c = solve(n,arr)
    print(f"Case #{case}: {c}")