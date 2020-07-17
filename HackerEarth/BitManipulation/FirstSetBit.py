def FirstSetBit(n):
	if n == 0:
		return 0
	def find_logbase2(n):
		m = 0
		while n >> 1:
			n >>= 1
			m += 1
		return m

	return int(find_logbase2(n & -n) + 1)


print(FirstSetBit(92))

# 	n = 92				--> 1011100
# 	-n (2s complement)	-->	0100100
# 	n&-n				-->	0000100
# 							-------
# 	log base 2					2+1		<-- 3