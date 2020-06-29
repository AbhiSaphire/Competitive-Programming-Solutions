def print_avg_sliding_window(l, n):

	suma = 0
	for i in range(n):
		suma += l[i]
		print("%.4f"%(suma/(i+1)), end = ' ')
	i, j = 1, n+1
	while j <= len(l):
		suma = sum(l[i:j])
		print("%.4f"%(suma/n), end = ' ')
		i, j = i+1, j+1

n = int(input())
l = [int(x) for x in input().split()]
print_avg_sliding_window(l, n)