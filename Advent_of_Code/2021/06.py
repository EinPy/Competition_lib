def setupInputOutputSublime():
	import sys
	sys.stdout = open("C:\\Temp\\output.txt", mode = 'w')
	sys.stdin = open("C:\\Temp\\input.txt", mode = 'r')
setupInputOutputSublime()


#Code starts here:
fish = list(map(int,input().split(',')))

for i in range(256):
	for i in range(len(fish)):
		if fish[i] == 0:
			fish[i] = 6
			fish.append(8)
		else:
			fish[i] -= 1

print(len(fish))
# 567111 is too high

