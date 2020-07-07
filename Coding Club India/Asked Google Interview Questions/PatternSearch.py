def PatternSearch(pat, text):
	i, j = 0, len(pat)
	while j < len(text):
		j = i+len(pat)
		if text[i:j] == pat:
			print("Found at index :", i+1)
		i+=1

PatternSearch("ABC", "ABCDEFABCDDGHSGABHHUABC")
# 1, 7, 21