import sys
itr = (line for line in sys.stdin.read().strip().split('\n'))
input = lambda: next(itr)


def solve(s):
    curRev = (0,0)
    best = 0
    found = False
    for i, v in enumerate(s):
        for j in range(i+1,len(s)):
            diff = v - s[j]
            if diff > best:
                curRev= (i,j)
                best = diff
                found = True
        if found:
            break
         
    if best == 0:
        s = list(map(str,s))
        print(' '.join(s))
 #       print("not better")
    else:
        l, r = curRev
        s = reverse(s, l, r)
        s = list(map(str,s))
        print(' '.join(s))


def reverse(a,l = 0,r = -1):
#    print(l,r)
    p1 = a[:l]
    p2 = a[l:r+1][::-1]
    p3 = a[r+1:]
    return p1 + p2 + p3

T = int(input())
for i in range(T):
    n = int(input())
    s = list(map(int,input().split()))
    solve(s)
    