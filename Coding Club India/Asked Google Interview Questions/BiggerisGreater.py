def BiggerisGreater(w):
	best = ''
	for i in range(len(w)):
		idx = -i-1
		c = w[idx]
		if c >= best:
			best = c
		else:
			l = sorted(w[idx:])
			print(*enumerate(l))
			for j, ch in enumerate(l):
				print("CH ", ch, " C ", c, " IDX ", idx)
				if ch > c:
					return w[:idx] + ch + ''.join(l[:j] + l[j+1:])
	return 'no answer'


print(BiggerisGreater("dkhc"))
print(BiggerisGreater("abcd"))
print(BiggerisGreater("zzeh"))

# (0, 'c') (1, 'd') (2, 'h') (3, 'k')
# CH  c  C  d  IDX  -4
# CH  d  C  d  IDX  -4
# CH  h  C  d  IDX  -4
# hcdk
# (0, 'c') (1, 'd')
# CH  c  C  c  IDX  -2
# CH  d  C  c  IDX  -2
# abdc
# (0, 'e') (1, 'h')
# CH  e  C  e  IDX  -2
# CH  h  C  e  IDX  -2
# zzhe