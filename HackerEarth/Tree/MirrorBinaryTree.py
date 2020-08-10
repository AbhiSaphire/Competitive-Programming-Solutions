# Python3 for Mirror Binary Tree
# 			  1								1
# 			 / \						   / \
# 			3	2			--->		  2	  3
# 		       / \						 / \
# 			  5	  4				   	    4   5


# RECURSIVE
def mirror(root):
	if not root: 
		return
	mirror(root.left)
	mirror(root.right)
	root.left, root.right = root.right, root.left


# ITERATIVE
def mirror(root):
	queue = []
	queue.append(root)
	while queue:
		q = queue.pop(0)
		if q.left:
			queue.append(q.left)
		if q.right:
			queue.append(q.right)
		q.left, q.right = q.right, q.left