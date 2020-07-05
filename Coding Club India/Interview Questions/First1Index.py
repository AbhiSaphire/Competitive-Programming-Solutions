def First1Index(arr, n):
	l, r = 0, n-1

	while l <= r:
		mid = (l+r) //2
		if arr[mid] == 1 and arr[mid-1] == 0:
			return mid
		elif arr[mid] == 0:
			l = mid+1
		else:
			r = mid-1


print(First1Index([0, 0, 0, 0, 0, 0, 1, 1, 1, 1], 10))