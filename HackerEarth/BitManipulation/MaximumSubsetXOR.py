def MaximumSubsetXOR(set, n):
	index = 0
	for i in range(31, -1, -1):
		MaxI = index
		MaxE = -999999999

		for j in range(index, n):
			if ((set[j] & (1 << i)) != 0 and set[j] > MaxE):
				MaxE = set[j]
				MaxI = j

		if MaxE == -999999999:
			continue
		set[index], set[MaxI] = set[MaxI], set[index]

		maxI = index
		for j in range(n):
			if (j != maxI and ((set[j] & (1 << i)) != 0)):
				set[j] = set[j] ^ set[maxI]

		index += 1
	res = 0
	for i in range(n):
		res ^= set[i]
	return res


print(MaximumSubsetXOR([2, 4, 5], 3))
print(MaximumSubsetXOR([9, 8, 5], 3))