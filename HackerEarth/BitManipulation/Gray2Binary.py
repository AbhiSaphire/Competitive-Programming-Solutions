def Gray2Binary(n):
	m = 0
	while n:
		m ^= n
		n >>= 1
	return m

print(Gray2Binary(4))