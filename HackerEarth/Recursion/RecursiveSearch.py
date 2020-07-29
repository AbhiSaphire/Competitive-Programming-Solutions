def RecursiveSearch(l, x):
	if not len(l):
		return False
	if l[0] == x:
		return True
	if l[-1] == x:
		return True
	return RecursiveSearch(l[1:-1], x)

print(RecursiveSearch([10, 22, 343, 421, 11, 6, 7, 8, 9, 10], 11))