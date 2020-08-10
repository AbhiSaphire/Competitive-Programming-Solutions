# Python3 Binary Tree to Doubly Linked List
# 				 10
# 			   /    \
# 			  12     15         ---> 		head ---> 25<->12<->30<->10<->36<->15 
#		     /  \   /
# 			25  30 36
# 		


def tree2DLL(root, head):
	if not root:
		return
	prev = None
	tree2DLL(root.left)
	if not prev:
		head = prev
	else:
		root.left = prev
		prev.right = root
	prev = root