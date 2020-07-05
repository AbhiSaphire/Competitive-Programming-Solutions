import collections
def MaxSumDigits(n):
	summ = []
	for i in range(1, n+1):
		temp = 0
		while int(i):
			temp  += i%10
			i = i//10
		summ.append(temp)

	curr = count = 0 
	for i in collections.Counter(summ).values():

		if i >= curr:
			count += 1
			curr = i

	return count

print(MaxSumDigits(13))