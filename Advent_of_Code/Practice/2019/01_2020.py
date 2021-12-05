def setupInputOutputSublime():
	import sys
	sys.stdout = open("C:\\Temp\\output.txt", mode = 'w')
	sys.stdin = open("C:\\Temp\\input.txt", mode = 'r')
setupInputOutputSublime()

#divide by three, round down, and subtract 2
things = []
for i in range(100):
	things.append(int(input()))


fueltot = 0

def part1():
	total = 0
	fueltot = 0
	for val in things:
		f = (val //3 ) - 2
		fueltot += f
		current = f
		while current > 0:
			current = (current // 3) - 2
			if current > 0:
	#			print("adding: ", current)
				fueltot += current

	return fueltot

def part2():
	pass

print(part1())
