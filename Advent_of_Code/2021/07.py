def setupInputOutputSublime():
	import sys
	sys.stdout = open("C:\\Temp\\output.txt", mode = 'w')
	sys.stdin = open("C:\\Temp\\input.txt", mode = 'r')
setupInputOutputSublime()


#Code starts here:

c = list(map(int,input().split(',')))

mid = len(c) // 2
target = c[mid]
costs = []

total = 0
for v in c:
	total += v 
avg = round(total / len(c))
print(avg)

#math formula for sum of arithmetic sequence:
# n * (a_1 + a_n) / 2


for a in range(avg - 10, avg + 10):
	cost = 0
	for v in c:
		cost += abs(v-a) * (1 + abs(v-a))/2
	costs.append(cost)
print(cost)
print(min(costs))
#96987919 too high
print(round(4.5))