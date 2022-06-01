t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))

    s = list(map(int, list(input())))
    steppish = 0
    r1 = -1

    tilfeldig = 0
    l1 = -1
    x = sum(s)
    if s[-1] == 0:
        for i in range(n - 1, -1, -1):
            if s[i] == 1:
                steppish = n - i - 1
                break
    else:
        steppish = 0
    if s[0] == 0:
        for i in range(0, n):
            if s[i] == 1:
                tilfeldig = i
                break
    else:
        tilfeldig = 0
    p = 0
    if x > 0:
        if steppish <= k:
            if tilfeldig <= k - steppish and x > 1:
                p = 11 * (x - 1)
            else:
                p = 1 + 11*(x - 1)
        elif tilfeldig <= k:
            p = 10 + 11 *(x - 1)
        else:
            p = x * 11
        print(p)
        
    else:
        print(0)