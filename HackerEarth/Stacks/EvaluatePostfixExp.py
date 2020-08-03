# Python3 Evaluate Postfix Expression

def Evaluate(exp):
	stack = []
	for i in exp:
		if i.isdigit():
			stack.append(int(i))
		else:
			b = stack.pop()
			a = stack.pop()
			if i == '+':
				stack.append(a+b)
			elif i == '-':
				stack.append(a-b)
			elif i == '*':
				stack.append(a*b)
			elif i == '/':
				stack.append(a//b)
			elif i == '^':
				stack.append(a^b)
	return stack[-1]

print(Evaluate("231*+9-"))