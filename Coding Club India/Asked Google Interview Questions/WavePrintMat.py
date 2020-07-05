def solution(mat):
	iswave = True
	for i in range(len(mat[0])):
		for j in range(len(mat)):
			if iswave == True:
				print(mat[j][i], end=' ')
			else:
				print(mat[len(mat)-j-1][i], end=' ')
			if j == len(mat)-1:
				iswave = not iswave
	print("END")

solution([[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34], [41, 42, 43, 44]])