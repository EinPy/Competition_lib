#input setup, not relevant for solution
import time
def setupInputOutputSublime():
	import sys
	sys.stdout = open("C:\\Temp\\output.txt", mode = 'w')
	sys.stdin = open("C:\\Temp\\input.txt", mode = 'r')
setupInputOutputSublime()

T = 200
nums = []
while T:
	nums.append(int(input()))
	T -= 1

def einar():
	nums.sort()

	for i , v in enumerate(nums):
		p2 = len(nums) - 1
		p1 = i + 1
		while p1 < p2:
			tot = v + nums[p1] + nums[p2]
			if tot  == 2020:
				print(v * nums[p1] * nums[p2])
				return
			elif tot > 2020:
				p2 -= 1
			else:
				p1 += 1

def erik():
	for i in range(0, len(nums)):
		for j in range(i+1, len(nums)):
			for k in range(j+1, len(nums)):
				if nums[i] + nums[j] + nums[k] == 2020:
					print(nums[i] * nums[j] * nums[k])
					return
einar()
print("what")
erik()