def calc(l, n):
	count = 0
	maxx = -1
	if n == 1:
		return 1
	for i in range(n):
		if i == n-1 and l[i] > maxx:
			count += 1
		elif i < n-1 and l[i] > l[i+1] and l[i] > maxx:
			count += 1
			
		maxx = max(maxx, l[i])
	return count

T = int(input())
for i in range(T):
	n = int(input())
	l = [int(x) for x in input().split()][:n]
	val = calc(l, n)
	print("Case #", end = '')
	print(i+1, end="") 
	print(":", val)