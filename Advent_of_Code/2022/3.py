import sys
tot = 0
for line in sys.stdin.read().strip().split('\n'):
    a = list((line[:len(line)//2]))
    b = list((line[len(line)//2:]))
    d = {}
    for l in a:
        if l not in d:
            d[l] = 1
    d2 = {}
    for l in b:
        if l in d and l not in d2:
            if l == l.upper():
                #print(l, ord(l) - ord("A") + 27)
                tot += ord(l) - ord("A")  + 27
            else:
                #print(l, ord(l) - ord("a") + 1)
                tot += ord(l) - ord("a") + 1
            d2[l] = 1
print(tot)
