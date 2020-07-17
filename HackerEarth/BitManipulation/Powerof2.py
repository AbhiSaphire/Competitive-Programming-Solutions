# Check whether given number is a Power of 2 or not

def Powerof2(n):
	def find_log(n):
		m = 0
		while n>>1:
			n >>= 1
			m += 1
		return m
	return True if 2**find_log(n) == n else False


print(Powerof2(1))
print(Powerof2(2))
print(Powerof2(64))
print(Powerof2(100))
print(Powerof2(1453452345483275834758923478527483957438197580913475891798347598173495871))