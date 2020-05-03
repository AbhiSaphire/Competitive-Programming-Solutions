# Solved in 56 min. using list comprehension
# Task was to return a list in same order after removing element whos occurance is > n
# data = [1, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6] and n = 3 return [1, 2, 3, 5, 6] removing 4 because count(4) > n

def solution(data, n):
	returner = []
	if n == 0:
		return returner

	return([x for x in data if data.count(x) <= n])



print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 0))
print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))
print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 2))
print(solution([], 2))
