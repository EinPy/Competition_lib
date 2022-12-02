for _ in range(int(input())):
    n, x = map(int, input().split())
    if n % x:
        print(-1)
        continue
    a = list(range(1, n + 1))
    if x == n:
        a[0], a[-1] = a[-1], a[0]
        print(*a)
        continue
 
    a[0], a[-1], a[x-1] = x, 1, n
    x -= 1
    print(a)
    for i in range(1, n-1):
        if a[x] % (i + 1) == 0 and a[i] % (x + 1) == 0:
            a[i], a[x] = a[x], a[i]
            x = i
    print(*a)