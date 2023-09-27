from heapq import heappush, heappop

n,m = map(int,input().split())

l = []
for _ in range(n):
    a,b = map(int,input().split())
    l.append((b,-a))
l.sort()
l = [(a,-b) for a,b in l]
#print(l)

def works(speed):
    h = []
    skips =m
    work = 0    
    for deadline,pages in l:
        work+=pages
        heappush(h,-pages)
        #print(work,deadline,speed,skips,h)
        while speed*deadline<work:
            #print("skip",speed,deadline,work)
            if skips == 0:
                return False
            work += heappop(h)
            skips -=1
    return True

lo,hi = 1,10**16
while lo < hi:
    mi = (lo+hi)//2
    if works(mi):
        hi = mi
    else:
        lo = mi+1

print(hi)
        