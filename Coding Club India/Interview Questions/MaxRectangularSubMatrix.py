def solution(M):

	def calc(A):
		stack = []
		max_area = 0
		index = 0
		while index < len(A):
			if not stack or (A[stack[-1]] < A[index]):
				stack.append(index)
				index += 1

			else:
				top_element = stack.pop()
				area = (A[top_element] * ((index - stack[-1]-1) if stack else index))
				max_area = max(max_area, area)

		while stack:
			top_element = stack.pop()
			area = (A[top_element] * ((index - stack[-1]-1) if stack else index))
			max_area = max(max_area, area)

		return max_area
	
	result = calc(M[0])
	for i in range(1, len(M)):
		for j in range(len(M[0])):
			if M[i][j] != 0:
				M[i][j] += M[i-1][j]
		result = max(result, calc(M[i]))

	print(result)

solution([[0, 1, 1, 0], 
         [1, 1, 1, 1],  
         [1, 1, 1, 1],  
         [1, 1, 0, 0]])

