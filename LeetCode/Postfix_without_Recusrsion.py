# ~~ABHISHEK K. SINGH~~
# Time complexity -- O(2n) ---> O(n) for creating stack2 and O(n) for printing stack2
# Auxilary Space -- O(2n) ---> O(n) for each stack

from binarytree import Node

def solution(root):
	print(root)
	if root is None:
		return
	stack1 = []
	stack2 = []

	stack1.append(root)
	while(stack1):
		top = stack1.pop()
		stack2.append(top)
		if top.left:
			stack1.append(top.left)
		if top.right:
			stack1.append(top.right)

	while stack2:
		print(stack2.pop().value, end=" ")

	print()

if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)
	solution(root)
