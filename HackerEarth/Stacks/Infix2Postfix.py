# Python3 INFIX -> POSTFIX Stack Implementation

def Infix2PostFix(exp):
	def prec(c):
		if c == '^':
			return 3
		elif c == '*' or c == '/':
			return 2
		elif c == '+' or c == '-':
			return 1
		else:
			return -1 

	stack = []
	stack.append('$')
	for i in exp:
		if (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z'):
			print(i, end='')
		elif i == '(':
			stack.append(i)
		elif i == ')':
			while stack[-1] != '$' and stack[-1] != '(':
				print(stack.pop(), end='')
			if stack[-1] == '(':
				stack.pop()
		else:
			while stack[-1] != '$' and prec(i) <= prec(stack[-1]):
				print(stack.pop(), end='')
			stack.append(i)

	while stack[-1] != '$':
		print(stack.pop(), end='')

Infix2PostFix("a+b*(c^d-e)^(f+g*h)-i")
print()
