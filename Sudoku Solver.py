import numpy as np

EMPTY = 0
N = 3
NUM_ROWS = N * N
NUM_COLS = N * N

puzzle = [[6,7,9,0,0,8,0,0,0],
		  [0,5,0,0,1,0,0,0,3],
		  [3,1,0,0,2,0,5,0,0],
		  [7,4,0,1,8,0,0,3,9],
		  [0,3,0,0,0,0,0,1,0],
		  [9,2,0,0,3,5,0,6,7],
		  [0,0,7,0,4,0,0,5,6],
		  [5,0,0,0,9,0,0,2,0],
		  [0,0,0,5,0,0,3,8,1]]

def solve() :
	global puzzle
	for row in range(NUM_ROWS) :
		for col in range(NUM_COLS) :
			if puzzle[row][col] == EMPTY :
				for num in range(1,10) :
					if canPut(num, row, col) :
						puzzle[row][col] = num
						solve()
						puzzle[row][col] = EMPTY
				return
	print(np.matrix(puzzle))


def canPut(num, row, col) :
	global puzzle

	return canPutInRow(num, row) and canPutInCol(num, col) and canPutInSquare(num, row, col)

def canPutInRow(num, row) :
	global puzzle

	for col in range(NUM_ROWS) :
		if puzzle[row][col] == num:
			return False

	return True

def canPutInCol(num, col) :
	global puzzle

	for row in range(NUM_COLS) :
		if puzzle[row][col] == num:
			return False

	return True

def canPutInSquare(num, row, col) :
	global puzzle

	startCol = ((col // N) * N)
	endCol = startCol + N
	startRow = ((row // N) * N)
	endRow = startRow + N

	for row in range(startRow, endRow) :
		for col in range(startCol, endCol) :
			if puzzle[row][col] == num :
				return False

	return True

solve()