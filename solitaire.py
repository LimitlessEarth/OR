import numpy as np

n = 10

board = np.ones((n, n))
board1 = np.triu(board, 0)

def padzeros(vector, pad_width, iaxis, kwargs):	
	vector[:pad_width[0]] = 0
	vector[-pad_width[1]] = 0
	return vector

board2 = np.lib.pad(board1, 2, padzeros)

possible_start = []

x = 0
y = 0

for i in board2:
	for j in i:
		if j == 1:
			possible_start.append((x, y))
		y += 1
	y = 0
	x += 1

print possible_start

print board2

#print board


