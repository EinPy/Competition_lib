n,s = map(int,input().split())
bids = []
for _ in range(n):
    name,b = input().split()
    b = int(b)
    bids.append((b,name))
bids.sort()
good = []

while s>0:
    if not bids:
        s = -1
        continue
    b,name = bids.pop()
    #print(name,b,s)
    if b>s:
        continue
    else:
        s-=b
        good.append(name)

if s<0:
    print(0)
else:
    print(len(good))
    print("\n".join(good))