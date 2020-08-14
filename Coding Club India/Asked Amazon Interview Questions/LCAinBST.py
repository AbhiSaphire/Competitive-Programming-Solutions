# Python3 Finding Lowest Common Ancestor in Binary Tree ----> O(N)
def find_lca_bt(root, n1, n2):
	if not root:
		return None

	left_lca = find_lca_bt(root.left, n1, n2)
	right_lca = find_lca_bt(root.right, n1, n2)

	if left_lca and right_lca:
		return root

	return left_lca if left_lca else right_lca


# Python3 Finding Lowest Common Ancestor in Binary Seacrh Tree ----> O(logN)
# 1. Recursive
def find_lca_bst(root, n1, n2):
	if not root:
		return None

	if root.data > n1 and root.data > n2:
		return find_lca_bst(root.left)
	if root.data < n1 and root.data < n2:
		return find_lca_bst(root.right)

	return root

# 2. Itterative
def find_lca_bst(root, n1, n2):
	while root:
		if root.data > n1 and root.data > n2:
			root = root.left
		elif root.data< n1 and root.data < n2:
			root = root.right
		else:
			break
	return root