import math

def MaxAreaHistogram(hist, n):
	stack = []
	index = 0
	max_area = 0
	while index < n:
		if not stack or hist[stack[-1]] <= hist[index]:
			stack.append(index)
			index += 1

		else:
			top_element = stack.pop()
			area = (hist[top_element])*((index-stack[-1]-1) if stack else index)

			max_area = max(max_area, area)

	while stack:
		top_element = stack.pop()
		area = (hist[top_element])*((index-stack[-1]-1) if stack else index)

		max_area = max(max_area, area)

	return max_area

print(MaxAreaHistogram([2, 3, 1, 4, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1 ,1 ,1 ,109, 1, 1, 1], 23))