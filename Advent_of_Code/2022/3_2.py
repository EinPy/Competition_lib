import sys
tot = 0
lC = 1
d = {}
dShared = {}
for line in sys.stdin.read().strip().split('\n'):
    if lC == 4:
        d = {}
        dShared = {}
        lC = 1
    a = list(line)
    if lC == 1:
        for l in a:
            if l not in d:
                d[l] = 1
    if lC == 2:
        for l in a:
            if l in d:
                dShared[l] = 1
    if lC == 3:
        for l in a:
            if l in dShared:
                #print(l)
                if l == l.upper():
                    #print(l, ord(l) - ord("A") + 27)
                    tot += ord(l) - ord("A")  + 27
                else:
                    #print(l, ord(l) - ord("a") + 1)
                    tot += ord(l) - ord("a") + 1
                break
    lC += 1
print(tot)
