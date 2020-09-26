# Python3 Longest Increasing Subsequence

def lis(arr):
	n = len(arr)
	lis = [0 for _ in range(n)]
	lis[0] = 1
	for i in range(1, n):
		lis[i] = 1
		for j in range(i):
			if arr[i] > arr[j] and lis[i] < lis[j] + 1:
				lis[i] = lis[j] + 1
	return max(lis)

print(lis([10, 22, 9, 33, 21, 50, 41, 60, 80]))							# -> 6
print(lis([10, 20, 30, 1, 2, 3, 4, 5, 6, 7, 8, 9, 50, 40, 100]))		# -> 11