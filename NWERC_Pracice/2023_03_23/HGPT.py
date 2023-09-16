MAXT = 101

a = [0] * MAXT
b = [0] * MAXT
ca = [0] * MAXT
cb = [0] * MAXT

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    a[x] += 1
    b[y] += 1

    for j in range(MAXT):
        ca[j] = a[j]
        cb[j] = b[j]

    sol = 0
    ap = MAXT - 1
    bp = 1

    while ap > 0 and bp < MAXT:
        while ap > 0 and not ca[ap]:
            ap -= 1
        while bp < MAXT and not cb[bp]:
            bp += 1

        if ap == 0 or bp == MAXT:
            break

        if ap + bp > sol:
            sol = ap + bp

        if ca[ap] > cb[bp]:
            ca[ap] -= cb[bp]
            cb[bp] = 0
        else:
            cb[bp] -= ca[ap]
            ca[ap] = 0

    print(sol)