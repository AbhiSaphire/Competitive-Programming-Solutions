# level 2 completed in 12 hours (including overnight sleep. LOL!)
# Basically Task was to sort a given list of strings of versions.
# Eg. list=["0.1.1", "3.3.2", "5.7.2", "0.3", "0.5.6", "1.3", "9.9"] produces ['0.1.1', '0.3', '0.5.6', '1.3', '3.3.2', '5.7.2', '9.9']
# My approach:: built a merge sort with custom compare function to split and comapre versions (since they are not int values)
# If someone find any better solution (time complexity < O(nlogn)) for that feel free to make a pull request.

def compare(x, y):
	a = x.split('.')
	b = y.split('.')

	i = j = 0
	while i < len(a) and j < len(b):
		if int(a[i]) > int(b[j]):
			return False
		elif int(b[j]) > int(a[i]):
			return True
		i += 1
		j += 1
	if i < len(a):
		return False
	return True

def combine(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m
	L = [0]*(n1)
	R = [0]*(n2)

	for i in range(0, n1):
		L[i] = arr[l + i]
	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	i = 0
	j = 0
	k = l

	while i<n1 and j<n2:
		if compare(L[i], R[j]):
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	while i<n1:
		arr[k] = L[i]
		i += 1
		k += 1
	while j<n2:
		arr[k] = R[j]
		j += 1
		k += 1

def sorting(arr, l, r):
	if l < r:
		m = (l + r) // 2
		sorting(arr, l, m)
		sorting(arr, m+1, r)
		combine(arr, l, m, r)

def solution(l):
	sorting(l, 0, len(l)-1)
	print(l)

solution(["0.1.1", "3.3.2", "5.7.2", "0.3", "0.5.6", "1.3", "9.9"])
solution([])
solution(["0.1.1", "0.1.1", "9.3"])
