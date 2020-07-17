def CheckKthBit(n, k):
	return True if n & (1 << k) else False

print(CheckKthBit(500, 3))