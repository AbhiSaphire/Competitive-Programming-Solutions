# Factorial Function With and Without Tail Recursion

# The tail-recursive functions are considered better than 
# non-tail recursive functions as tail-recursion can be 
# optimized by compiler. The idea used by compilers to 
# optimize tail-recursive functions is simple, since the
# recursive call is the last statement, there is nothing 
# left to do in the current function, so saving the current 
# function’s stack frame is of no use.


def NotTailFactorial(n):
	if n <= 1:
		return 1
	return n*NotTailFactorial(n-1)

def TailFactorial(n, a):
	if n <= 1:
		return a
	return TailFactorial(n-1, n*a)

print(NotTailFactorial(20))
print(TailFactorial(20, 1))

print(NotTailFactorial(30))
print(TailFactorial(30, 1))