def find_prime(n): 
	if n == 1:
		print(1)
		return
	prime = [True for i in range(n+1)] 
	p = 2
	while (p * p <= n): 
		if prime[p]: 
			for i in range(p * p, n+1, p): 
				prime[i] = False
		p += 1
	print(sum(prime[2:]))

t = int(input())
while t:
	n = int(input())
	find_prime(n)
	t -= 1