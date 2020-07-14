def calc(l, n):
	min_count = 999999999999
	tone = ['A', 'B', 'C', 'D']
	x = 1
	while x < len(tone):
		temp_count = 0
		i = x
		for j in range(1, n):
			print(i, " ", l[j], end=" ")
			if l[j] > l[j-1] and i+1 < len(tone):
				i += 1
			elif l[j] < l[j-1] and i-1 >= 0:
				i -= 1
			elif l[j] > l[j-1] and not i+1 < len(tone):
				temp_count += 1
				i = 0
			elif l[j] < l[j-1] and not i-1 >= 0:
				temp_count += 1
				i = len(tone)-1
			print(temp_count)
		min_count = min(min_count, temp_count)
		x += 1
	return min_count


T = int(input())
for i in range(T):
	k = int(input())
	l = [int(x) for x in input().split()][:k]
	val = calc(l, k)
	print("Case #", end = '')
	print(i+1, end="") 
	print(":", val)


# 2
# 5
# 1 5 100 500 1
# 8
# 2 3 4 5 6 7 8 9