# Bunny - Prisoner - Locating solved in 3 hours and 40 mins
# Task was to return element at a certain place in a given pattern
# 16
# 11  17
# 07  12  18
# 04  08  13  19
# 02  05  09  14  20
# 01  03  06  10  21
# Tried solving this question by making a binary tree(was a lot lengthy) then my brother came up with this simple Arithmetic progression solution
# First we find diagonal corner of searched element and then move diagonally reducing 1 at a time to get to the searched element.

def solution(x, y):
	diagonal_difference = y - 1
	element_row = x + diagonal_difference
	value = element_row * (element_row + 1) // 2
	value -= diagonal_difference
	return str(value)

print(solution(10, 10))
print(solution(10000, 10000))
print(solution(1, 1))
print(solution(1, 10000))
