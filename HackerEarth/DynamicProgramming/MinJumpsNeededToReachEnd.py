# Python3 Minimum Number of Jumps needed to reach End

# Given an array of integers where each element represents the max number
# of steps that can be made forward from that element. Write a function to
# return the minimum number of jumps to reach the end of the array (starting
# from the first element). If an element is 0, then cannot move through that element.

def MinJumps(arr):
	n = len(arr)
	if n == 0 or arr[0] == 0:
		return -1

	jumps = [0 for _ in range(n)]
	for i in range(1, n):
		jumps[i] = float('inf')
		for j in range(i):
			# print(i, j, arr[j], jumps[j])
			if i <= j + arr[j] and jumps[j] != float('inf'):
				jumps[i] = min(jumps[i], jumps[j] + 1)
				break

	return jumps[n-1]

print(MinJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))