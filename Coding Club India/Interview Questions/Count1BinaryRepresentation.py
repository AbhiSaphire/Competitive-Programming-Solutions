def calculate(n, summ):
	if n <= 1:
		return n
	summ += calculate(n//2, summ)
	summ += n%2
	return summ

print(calculate(7, 0))