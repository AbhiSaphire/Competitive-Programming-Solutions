if __name__ == "__main__":
	l = [int(x) for x in input().split()]
	def isValidMaxHeap(l, n):
		for i in range(((n-2)//2)+1):
			if l[2*i+1] > l[i]:
				return False
			if 2*i+2 < n and l[2*i+2] > l[i]:
				return False
		return True
	print(isValidMaxHeap(l, len(l)))