# Incomplete solution (Min-Heap Solution) --> O(n) time

from heapq import heapify, heappush, heappop

def KthSmallestArraySumofMatrix(mat, k):
	heap = []
	heapify(heap)
	for i in range(len(mat)):
		for j in range(len(mat[0])):
			heappush(heap, mat[i][j])

	heapify(heap)
	print(heap)

	for i in range(k):
		element = heappop(heap)
		heapify(heap)

	return element


print(KthSmallestArraySumofMatrix([[1, 3, 11], 
									[2, 4, 6]], 5))

# [3, 5, 5, 7, 7, 9, 13, 15, 17] ---> 5th Smallest Sum --> 7