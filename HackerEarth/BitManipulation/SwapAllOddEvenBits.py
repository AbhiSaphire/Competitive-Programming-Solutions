def SwapOddEvenBits(n):
	even = n & 0xAAAAAAAA
	odd  = n & 0x55555555
	even >>= 1
	odd  <<= 1

	return (even | odd)

print(SwapOddEvenBits(30))
print(SwapOddEvenBits(20))