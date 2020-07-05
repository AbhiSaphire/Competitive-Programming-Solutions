import sys
from heapq import heapify, heappop, heappush

# ---------------------------------------------Implementation of MAX_HEAP---------------------------------------

class MaxHeap:
	def __init__(self, maxsize):
		self.maxsize = maxsize
		self.size = 0
		self.Heap = [0]*(self.maxsize+1)
		self.Heap[0] = sys.maxsize
		self.FRONT = 1

	def parent(self, pos):
		return pos//2

	def leftchild(self, pos):
		return 2*pos

	def rightchild(self, pos):
		return (2*pos)+1

	def isLeaf(self, pos):
		if pos >= (self.size//2) and pos < self.size:
			return True
		return False

	def swap(self, fpos, spos):
		self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

	def heapify(self, pos):
		if not self.isLeaf(pos):
			if self.Heap[pos] < self.Heap[self.leftchild(pos)] or self.Heap[pos] < self.Heap[self.rightchild(pos)]:
				if self.Heap[self.leftchild(pos)] > self.Heap[self.rightchild(pos)]:
					self.swap(pos, self.leftchild(pos))
					self.heapify(self.leftchild(pos))
				else:
					self.swap(pos, self.rightchild(pos))
					self.heapify(self.rightchild(pos))

	def insert(self, value):
		if self.size >= self.maxsize:
			return
		self.size += 1
		self.Heap[self.size] = value
		current = self.size
		while self.Heap[current] > self.Heap[self.parent(current)]:
			self.swap(current, self.parent(current))
			current = self.parent(current)

	def Print(self):
		for i in range(1, (self.size//2)+1):
			print("PARENT : " + str(self.Heap[i]) + " LEFT : " + str(self.Heap[2*i]) + " RIGHT : " + str(self.Heap[2*i+1]))

	def extractMax(self):
		popped = self.Heap[self.FRONT]
		self.Heap[self.FRONT] = self.Heap[self.size]
		self.size -= 1
		self.heapify(self.FRONT)
		return popped

# -----------------------------------------------------Imported HEAPQ--------------------------------------------------

def printKLargest(l, k):
	newHeap = []
	heapify(newHeap)
	for i in l:
		heappush(newHeap, -1 * i)
	for _ in range(k):
		print(-1 *heappop(newHeap), end=' ')
	print()

# ------------------------------------------------------Driver Function-----------------------------------------------

if __name__ == "__main__":
	n, k = input().split()
	n, k = int(n), int(k)
	l = [int(x) for x in input().split()][:n]
	Heap = MaxHeap(n)
	for i in l:
		Heap.insert(i)
	for _ in range(k):
		print(Heap.extractMax(), end=" ")
	print()

	printKLargest(l, k)