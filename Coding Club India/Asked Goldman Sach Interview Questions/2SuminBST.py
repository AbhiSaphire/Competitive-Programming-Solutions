def inorder(head, arr):
	if  head:
		inorder(head.left, arr)
		arr.append(head, arr)
		inorder(head.right, arr)
	return arr


def 2SumBST(head1, head2, summ):
	arr1 = []
	arr2 = []
	arr1 = inorder(head1, arr1)
	arr2 = inorder(head2, arr2)

	i, j = 0, len(arr2)-1

	while i < len(arr1) and j >= 0:
		add = arr1[i] + arr2[i]
		if add == summ:
			return arr1[i], arr2[j]
		elif add > summ:
			j -= 1
		else:
			i += 1

# Sample Code (Does not work because NodeBST class is not implemented)
head1 = NodeBST()
head2 = NodeBST()
print(2SumBST(head1, head2, 10))