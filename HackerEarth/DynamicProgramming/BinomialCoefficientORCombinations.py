# Python3 for Finding Binomial Coefficient 
# 1. A binomial coefficient C(n, k) can be defined as the coefficient of X^k
# in the expansion of (1 + X)^n.

# 2. A binomial coefficient C(n, k) also gives the number of ways, disregarding
# order, that k objects can be chosen from among n objects; more formally, the 
# number of k-element subsets (or k-combinations) of an n-element set.

def Binomial(n, k):
	C = [[-1 for _ in range(k+1)] for _ in range(n+1)]
	for i in range(n+1):
		for j in range(min(i, k)+1):
			if j == 0 or j == i:
				C[i][j] = 1
			else:
				C[i][j] = C[i-1][j-1] + C[i-1][j]

	return C[n][k]
print(Binomial(5, 2))