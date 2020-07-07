def RabinKarpPatternSearch(text, pat, q):
	d = 256
	N = len(text)
	M = len(pat)
	p = t = 0
	h = 1

	for i in range(M-1):
		h = (h*d)%q

	for i in range(M):
		p = (d*p + ord(pat[i]))%q
		t = (d*t + ord(text[i]))%q

	for i in range(N-M+1):
		if p == t:
			for j in range(M):
				if text[i+j] != pat[j]:
					break
			j += 1
			if j == M:
				print("Found at index : ", str(i+1))

		if i < N-M:
			t = (d*(t - ord(text[i])*h) + ord(text[i+M]))%q
			if t < 0:
				t += q

RabinKarpPatternSearch("ABCABCBBHDKKSJJBCBBBCABBCABCABCBBBNNBCVAVCKJIJABC", "ABC", 101)