def setupInputOutputSublime():
	import sys
	sys.stdout = open("C:\\Temp\\output.txt", mode = 'w')
	sys.stdin = open("C:\\Temp\\input.txt", mode = 'r')
setupInputOutputSublime()


#Code starts here:
fish = list(map(int,input().split(',')))

def naive_solution(fish):
	for i in range(80):
		for i in range(len(fish)):
			if fish[i] == 0:
				fish[i] = 6
				fish.append(8)
			else:
				fish[i] -= 1

	print(len(fish))


def part2(fish):
	"""
	for one fish, if only doubling every 6 days
	amount(n) = 2*(n%6)
	recursion? 
	"""
	#storing the values in a hash_map instead
	fishes = {}
	for i in range(9):
		fishes[i] = 0
	

	for val in fish:
		fishes[val] += 1

	for days in range(256):
		#ugly, would have been better to make a copy of the 
		#entire dictoinary instead, but gets it done. 
		zero, one, two = fishes[0], fishes[1], fishes[2]
		three, four, five = fishes[3], fishes[4], fishes[5]
		six, seven, eight = fishes[6], fishes[7], fishes[8]

		fishes[0] = one 
		fishes[1] = two
		fishes[2] = three
		fishes[3] = four
		fishes[4] = five
		fishes[5] = six
		fishes[6] = seven + zero
		fishes[7] = eight
		fishes[8] = zero	


	tot = 0
	for i in range(9):
		tot += fishes[i]	
	print(tot)


part2(fish)

def part2_better(fish):
	fishes = {}
	for i in range(9):
		fishes[i] = 0

	for val in fish:
		fishes[val] += 1

	for days in range(256):
		cop = fishes.copy()

		for i in range(9):
			if i == 6:
				fishes[i] = cop[7] + cop[0]
			elif i == 8:
				fishes[i] = cop[0]
			else:
				fishes[i] = cop[i+1]

	tot = 0
	for i in range(9):
		tot += fishes[i]	
	print(tot)
part2_better(fish)