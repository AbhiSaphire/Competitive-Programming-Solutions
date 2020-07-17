def Binary2Gray(n):
	return n^(n>>1)

print(Binary2Gray(4))