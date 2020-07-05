from heapq import heapify, heappop, heappush

n, k = input().split()
n, k = int(n), int(k)
l = [int(x) for x in input().split()][:n]
Heap = []
heapify(Heap)

for i in l:
	heappush(Heap, i)
for _ in range(k):
	print(heappop(Heap), end = ' ')
print()