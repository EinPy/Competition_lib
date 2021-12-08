def setupInputOutputSublime():
	import sys
	sys.stdout = open("C:\\Temp\\output.txt", mode = 'w')
	sys.stdin = open("C:\\Temp\\input.txt", mode = 'r')
setupInputOutputSublime()


#Code starts here:

combinations = []

for entry in range(200):
	line = input().split('|')
	line = [line[0].split()] + [line[1].split()]
	combinations.append(line)

u = {2: 1, 4: 4, 3 : 7, 7 : 8}
total = 0

for element in combinations:
	for output in element[1]:
		if len(output) in u:
			total += 1

print(total)
