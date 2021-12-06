def setupInputOutputSublime():
	import sys
	sys.stdout = open("C:\\Temp\\output.txt", mode = 'w')
	sys.stdin = open("C:\\Temp\\input.txt", mode = 'r')
setupInputOutputSublime()


#Code starts here:
vents = []

#test = input().split(' -> ')
#test[0] = list(map(int,test[0].split(',')))
#test[1] = list(map(int,test[1].split(',')))
#print(test)

for row in range(500):
	line = input().split(' -> ')
	line[0] = list(map(int,line[0].split(',')))
	line[1] = list(map(int,line[1].split(',')))
	vents.append(line)

def part1():
	bottom = {}
	for line in vents:
		if line[0][0] == line[1][0] and line[0][1] == line[1][1]:
			location = (line[0][0], line[0][1])
			if location in bottom:
				bottom[location] += 1
			else:
				bottom[location] = 1
		elif line[0][0] == line[1][0]:
			if line[0][1] <= line[1][1]:
				for y in range(line[0][1], line[1][1] + 1):
					location = (line[0][0], y)
					if location in bottom:
						bottom[location] += 1
					else:
						bottom[location] = 1
			else:
				for y in range(line[1][1], line[0][1] + 1):
					location = (line[0][0], y)
					if location in bottom:
						bottom[location] += 1
					else:
						bottom[location] = 1

		elif line[0][1] == line[1][1]:
			if line[0][0] <= line[1][0]:
				for x in range(line[0][0], line[1][0] + 1):
					location = (x, line[1][1])
					if location in bottom:
						bottom[location] += 1
					else:
						bottom[location] = 1
			else:
				for x in range(line[1][0], line[0][0] + 1):
					location = (x, line[1][1])
					if location in bottom:
						bottom[location] += 1
					else:
						bottom[location] = 1

	overlaps = 0
	for loc in bottom.keys():
		if bottom[loc] >= 2:
			overlaps+= 1
	print(overlaps)


def part2():
	bottom = {}
	for line in vents:
		#a point
		if line[0][0] == line[1][0] and line[0][1] == line[1][1]:
			location = (line[0][0], line[0][1])
			if location in bottom:
				bottom[location] += 1
			else:
				bottom[location] = 1
		#line is vertical
		elif line[0][0] == line[1][0]:
			if line[0][1] <= line[1][1]:
				for y in range(line[0][1], line[1][1] + 1):
					location = (line[0][0], y)
					if location in bottom:
						bottom[location] += 1
					else:
						bottom[location] = 1
			else:
				for y in range(line[1][1], line[0][1] + 1):
					location = (line[0][0], y)
					if location in bottom:
						bottom[location] += 1
					else:
						bottom[location] = 1
		#line is horizontal
		elif line[0][1] == line[1][1]:
			if line[0][0] <= line[1][0]:
				for x in range(line[0][0], line[1][0] + 1):
					location = (x, line[1][1])
					if location in bottom:
						bottom[location] += 1
					else:
						bottom[location] = 1
			else:
				for x in range(line[1][0], line[0][0] + 1):
					location = (x, line[1][1])
					if location in bottom:
						bottom[location] += 1
					else:
						bottom[location] = 1
		#line is diagonal
		else:
			if line[0][0] < line[1][0]:
				if line[0][1] < line[1][1]:
					for x, y in zip(range(line[0][0], line[1][0]+1), range(line[0][1],line[1][1]+1)):
						loc = (x,y)
						if loc in bottom:
							bottom[loc] += 1
						else:
							bottom[loc] = 1
				else:
					for x, y in zip(range(line[0][0], line[1][0]+1), range(line[0][1],line[1][1]-1, -1)):
						loc = (x,y)
						if loc in bottom:
							bottom[loc] += 1
						else:
							bottom[loc] = 1
			else:
				if line[0][1] > line[1][1]:
					for x, y in zip(range(line[1][0], line[0][0]+1), range(line[1][1],line[0][1]+1)):
						loc = (x,y)
						if loc in bottom:
							bottom[loc] += 1
						else:
							bottom[loc] = 1
				else:
					for x, y in zip(range(line[1][0], line[0][0]+1), range(line[1][1],line[0][1]-1, -1)):
						loc = (x,y)
						if loc in bottom:
							bottom[loc] += 1
						else:
							bottom[loc] = 1				



	overlaps = 0
	for loc in bottom.keys():
		if bottom[loc] >= 2:
			overlaps+= 1
	print(overlaps)
	print(bottom)

part2()

