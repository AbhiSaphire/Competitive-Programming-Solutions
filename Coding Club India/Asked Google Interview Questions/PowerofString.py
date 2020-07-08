def PowerofString(s):
	seen = {}
	max_power = 0
	i = 0
	for j in range(len(s)):
		if s[j] in seen:
			i = max(i, seen[s[j]]+1)
		seen[s[j]] = j
		max_power = max(max_power, j-i+1)

	return max_power

print(PowerofString("abcbbcdbbacbdef"))