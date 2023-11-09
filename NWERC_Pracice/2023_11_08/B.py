import heapq as h
q = []
h.heapify(q)
h.heappush(q,(2,3))
h.heappush(q,(5,10))
print(q[0])
print(h.heappop(q))
print(h.heappop(q))
