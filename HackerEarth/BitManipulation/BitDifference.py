def BitDifference(a, b):
	def CountBits(n):
		count = 0
		while n:
			count += n & 1
			n >>= 1
		return count

	return CountBits(a^b)


print(BitDifference(5, 15))

# 5		-->	0101
# 15	-->	1111
# 			----
# 			1010	<-- 2