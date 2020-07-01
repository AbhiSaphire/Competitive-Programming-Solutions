# def fact(n):
# 	if n == 1:
# 		return 1
# 	return n * fact(n-1)

def solution(arr, n):
	for i in range(n):
		temp = arr[abs(arr[i]) - 1]
		if temp < 0:
			repeating = abs(arr[i])
			continue

		arr[abs(arr[i]) -1] = -arr[abs(arr[i]) -1]

	for i in range(n):
		if arr[i] > 0:
			missing = i+1

	print("Missing - ", missing, "Repeating - ", repeating) 


solution([2, 3, 2, 1, 5], 5)