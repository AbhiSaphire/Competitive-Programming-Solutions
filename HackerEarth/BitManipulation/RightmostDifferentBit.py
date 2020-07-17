def RightmostDifferentBit(m, n):
	if m == n:
		return -1
	def RightmostBit(n):
		def logbase2(n):
			m = 0
			while n >> 1:
				n >>= 1
				m += 1
			
			return m

		return int(logbase2(n&-n)+1)
	
	return RightmostBit(m^n)

print(RightmostDifferentBit(52, 4))