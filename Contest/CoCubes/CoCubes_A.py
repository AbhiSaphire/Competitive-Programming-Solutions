def MCQResult(n, key, paper):
	i = 0
	sum = 0
	while i < n:
		if key[i] == paper[i]:
			sum += 3
		elif paper[i] == -1:
			continue
		else:
			sum -= 1
		i += 1
	return sum

print(MCQResult(5, [1, 3, 2, 1, 4], [1, 2, 2, 3, 3]))
print(MCQResult(4, [4, 2, 1, 2], [4, 2, 2, 2]))