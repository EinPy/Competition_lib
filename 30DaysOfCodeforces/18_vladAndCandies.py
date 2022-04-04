import sys
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)

#code


def solve(nums):
    m = 0
    for n in nums:
        m = max(m,n)
    if m-1 in nums or (len(nums) == 1 and nums[0] == 1) or nums.count(m) > 1:
        print("YES")
    else:
        print("NO")

    
T = int(input())
for case in range(T):
    trash = int(input())
    n = list(map(int,input().split()))
    solve(n)