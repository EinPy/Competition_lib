def setupInputOutputSublime():
	import sys
	sys.stdout = open("C:\\Temp\\output.txt", mode = 'w')
	sys.stdin = open("C:\\Temp\\input.txt", mode = 'r')
setupInputOutputSublime()


#Code starts here:
nums = list(map(int,input().split(',')))

boards = []
newBoard = []
lines = 0
for i in range(600):
	row = input()
	if row == '': #start new board
		lines = 0
		newBoard = []
	if lines < 5 and row != '':
		add = list(map(int,row.split()))
		for i, element in enumerate(add):
			add[i] = [element, False]
		newBoard.append(add)
		lines += 1
	if len(newBoard) == 5:
		boards.append(newBoard)

#for i in boards:
#	for row in i:
#		print(row)
#	print('\n')


def win_check(board):
	#checking if a row is win
	for row in board:
		rowWin = True
		for n in row:
			if n[1] == False:
				rowWin = False
		if rowWin:
#			print('rowWin')
			return True
	#checking if col is win
	cols = [True for _ in range(5)]
#	print(cols)
	for row in board:
		for j, val in enumerate(row):
			if val[1] == False:
				cols[j] = False
	for el in cols:
		if el == True:
#			print('colwin')
			return True
	return False

testboard = [[[50, False], [98, False], [65, False], [14, False], [47, False]],
[[0, False], [22, False], [3, False], [83, False], [46, False]],
[[87, False], [93, False], [81, False], [84, False], [58, False]],
[[40, False], [35, False], [28, False], [74, False], [48, False]],
[[45, False], [99, False], [59, False], [37, False], [64, False]]]
#for row in testboard:
#	print(row)
#print(win_check(testboard))
def play():
	for val in nums:
		for board in boards:
			for row in board:
				for element in row:
					if element[0] == val:
						element[1] = True
			if win_check(board):
				print('there is a winner')
				tot = 0
				for row in board:
					for i in row:
						if i[1] == False:
							tot += i[0]
				return(tot * val)

def last_winner():
	amount_of_boards = len(boards)
	print(amount_of_boards)
	wins = 0
	winners = {}
	for val in nums:
		for i, board in enumerate(boards):
			if i not in winners:
				for row in board:
					for element in row:
						if element[0] == val:
							element[1] = True
				if win_check(board):
					wins += 1
					print(wins)
					if wins == amount_of_boards:
						tot = 0
						for row in board:
							for i in row:
								if i[1] == False:
									tot += i[0]
						return(tot * val)
					else:
						winners[i] = True
print(last_winner())