# Python3 Minimize Sum using max-Heap

import heapq

def MinimizeSum(heap, n, k):
	heapq._heapify_max(heap)
	for i in range(k):
		if heap[0] == 1:
			break
		heap[0] = heap[0] >> 1
		heapq._siftup_max(heap, 0)
	return sum(heap)

if __name__ == "__main__":
	n, k = input().split()
	n, k = int(n), int(k)
	arr = [int(x) for x in input().split()][:n]
	print(MinimizeSum(arr, n, k))