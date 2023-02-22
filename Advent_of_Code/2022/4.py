import sys
tot = 0
for line in sys.stdin.read().strip().split('\n'):
    a, b =  line.split(",")
    a1, a2 = map(int,a.split("-"))
    b1, b2 = map(int,b.split("-"))
    if a1 >= b1 and a1 <= b2:
        tot += 1
    elif a2 >= b1 and a2 <= b2:
        tot += 1
    elif b1 >= a1 and b1 <= a2:
        tot += 1
    elif b2 >= a1 and b2 <= a2:
        tot += 1
print(tot)
    