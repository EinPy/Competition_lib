def setupInputOutputSublime():
	import sys
	sys.stdout = open("C:\\Temp\\output.txt", mode = 'w')
	sys.stdin = open("C:\\Temp\\input.txt", mode = 'r')
setupInputOutputSublime()

coms = input().split(",")

#board = [["." for i in range(10)] for i in range(10)]

for i in range(10, 5):
	print (i)

start = (0,0) #x, y
pos = (0,0) #x, y
been1 = {}
for c in coms:
	cur  = pos
	if c[0] == "R":
		pos = (pos[0] + int(c[1:]), pos[1])
		for i in range(cur[0], pos[0] + 1):
			been1[(cur[0] + abs(i), pos[1])] = True
	if c[0] == "L":
		pos = (pos[0] - int(c[1:]), pos[1])
		for i in range(cur[0], pos[0] -1, -1):
			been1[(cur[0] - abs(i), pos[1])] = True
	if c[0] == "U":
		pos = (pos[0], pos[1] + int(c[1:]))
		for i in range(cur[1], pos[1] + 1):
			been1[(pos[0], cur[1] + abs(i))] = True
	if c[0] == "D":
		pos = (pos[0], pos[1] - int(c[1:]))
		for i in range(cur[1], pos[1] -1, -1):
			been1[(pos[0], cur[1] - abs(i))] = True

coms2 = input().split(",")
#print(coms2)
start = (0,0) #x, y
pos = (0,0) #x, y
been2 = {}
for c in coms2:
	cur  = pos
	if c[0] == "R":
		pos = (pos[0] + int(c[1:]), pos[1])
		for i in range(cur[0], pos[0] + 1):
			been2[(cur[0] + abs(i), pos[1])] = True
	if c[0] == "L":
		pos = (pos[0] - int(c[1:]), pos[1])
		for i in range(cur[0], pos[0] -1, -1):
			been2[(cur[0] - abs(i), pos[1])] = True
	if c[0] == "U":
		pos = (pos[0], pos[1] + int(c[1:]))
		for i in range(cur[1], pos[1] + 1):
			been2[(pos[0], cur[1] + abs(i))] = True
	if c[0] == "D":
		pos = (pos[0], pos[1] - int(c[1:]))
		for i in range(cur[1], pos[1] -1, -1):
			been2[(pos[0], cur[1] - abs(i))] = True

#print(been2)
been1[(0,0)] = False
been2[(0,0)] = False
shortest = 1e19
for i in been1.keys():
	if been1[i] and i in been2:
#		print(i)
		shortest = min(shortest, abs(i[0]) + abs(i[1]))

print(shortest)
