n, arr = input(), list(map(int, input().split()))
lookup = {}
for i in range(257):
    lookup[i ^ (i << 1)%256] = i
print(" ".join(map(str,[lookup[a] for a in arr])))