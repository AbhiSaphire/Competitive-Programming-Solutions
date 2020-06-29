def solution(arr, n):
	maxx = arr[0]
	summ = 1
	for i in range(1, n):
		if arr[i] > maxx:
			summ += 1
	return summ

arr = [7, 4, 8, 2, 9]
print(solution(arr, len(arr)))