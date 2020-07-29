def solution(mat):
	n, q = [int(x) for x in input().split()]
	res = 0
	for _ in range(q):
		val = list(map(int, input().split()))
		if val[0] == 1:
			for i in mat:
				res += sum(i)
			print(res)
		elif val[0] == 2:
			mat[val[1]-1][val[2]-1] = 1
		elif val[0] == 3:
			for i in range(len(mat[val[1]])):
				mat[val[1]-1][i] = 1
		res = 0

solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

