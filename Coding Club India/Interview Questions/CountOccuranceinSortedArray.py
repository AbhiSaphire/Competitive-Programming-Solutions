def first_occurance(arr, x, l, r, n):
	while l <= r:
		mid = (l+r)//2
		if (arr[mid] == x and x > arr[mid-1] or mid == 0):
			return mid
		elif x > arr[mid]:
			return first_occurance(arr, x, mid+1, r, n)
		else:
			return first_occurance(arr, x, l, mid-1, n)


def last_occurance(arr, x, l, r, n):
	while l <= r:
		mid = (l+r) //2
		if (mid == n-1 or arr[mid] == x and x < arr[mid+1]):
			return mid
		elif x < arr[mid+1]:
			return last_occurance(arr, x, l, mid-1, n)
		else:
			return last_occurance(arr, x, mid+1, r, n)


def CountOccuranceSortedArray(arr, x):
	i = first_occurance(arr, x, 0, len(arr)-1, len(arr))
	j = last_occurance(arr, x, 0, len(arr)-1, len(arr))
	result = j - i + 1
	print("Number of Occurances - ", result)


CountOccuranceSortedArray([1,1,2,2,2,2,3,3,3,3], 2)