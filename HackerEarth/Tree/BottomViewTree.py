# Python3 Bottom View Binary Tree

class Node:
	def __init__(self, hd, data):
		self.left = None
		self.right = None
		self.hd = hd
		self.data = data

def BottomViewTree(root):
	if not root:
		return 
	q = []
	m = {}
	hd = 0
	root.hd = hd
	q.append(root)
	while q:
		hd = root.hd
		m[hd] = root.data
		if root.left:
			root.left = hd - 1
			q.append(root.left)
		if root.right:
			root.right = hd + 1
			q.append(root.right)
		q.pop(0)
		root = q[0]

	print(*m.values()) 