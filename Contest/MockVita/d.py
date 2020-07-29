from math import factorial

def gcd(t, m):
	if t==0 or m==0 : return 0
	if t == m : return t
	if t>m:
		return gcd(t-m, m)
	return gcd(t, m-t)

def iscoprime(t, m):
	if gcd(t, m) == 1:
		return True
	return False

def modInverse(m, mod):
	res = (m%mod + mod) % mod
	return res

def find_prob(m, t):
	if iscoprime(t, m):
		mod = 1000000007
		result = (t * modInverse(m, mod))% mod
		return result
	else:
		return m/t

def getprob(u, n, t):
	probA = factorial(u)*factorial(n-t)
	probB = factorial(n)*factorial(u-t)
	g = gcd(probA, probB)
	probA //= g
	probB //= g
	return probA, probB


test = int(input())
while test:
	n, t, m = input().split()
	u = int(n) - int(m)
	probA, probB = getprob(u, int(n), int(t))
	print(find_prob(probA, probB))
	test -= 1