arr = [int(x) for x in input().split()]
for i in range(0, len(arr)-1, 2):
	if arr[i] < arr[i-1] and i > 0:
		arr[i], arr[i-1] = arr[i-1], arr[i]
	if arr[i] < arr[i+1]:
		arr[i], arr[i+1] = arr[i+1], arr[i]

print(arr)