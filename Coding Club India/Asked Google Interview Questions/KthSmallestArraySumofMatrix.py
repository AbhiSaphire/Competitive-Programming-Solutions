# Incomplete solution (Min-Heap Solution) --> O(n) time
# Completed solution  (Cross Product Rows) --> O(n^2) time [Optimized]

from heapq import heapify, heappush, heappop
from itertools import product

def KthSmallestArraySumofMatrix(mat, k):
	heap = []
	heapify(heap)
	for i in range(len(mat)):
		for j in range(len(mat[0])):
			heappush(heap, mat[i][j])

	heapify(heap)

	for i in range(k):
		element = heappop(heap)
		heapify(heap)

	return element

def KthSmallestArraySumofMatrix_NAIVE(mat, k):
	return sorted([sum(x) for x in product(*mat)])[k-1]


print("Incorrect --> ", KthSmallestArraySumofMatrix([	[1, 3, 11], 
									[2, 4, 6]], 5))
# [3, 5, 5, 7, 7, 9, 13, 15, 17] ---> 5th Smallest Sum --> 7

print("Correct --> ", KthSmallestArraySumofMatrix_NAIVE([[1, 3, 11],
										[2, 4, 6]], 5))