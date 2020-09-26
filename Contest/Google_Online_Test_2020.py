# You are given an array A with N intergers. You are requested to answer Q 
# queries of the following type -> (L 	R)
# Determine the count of distinct prime numbers that divide all the array values from index L to R.
# Note : Consider 1 based indexing 

def seive(n): 
    prime =[True]*(n + 1) 
    p = 2
    while(p * p<= n): 
        if(prime[p] == True): 
            for i in range(p * p, n + 1, p): 
                prime[i] = False
        p += 1
    allPrimes = [x for x in range(2, n)if prime[x]] 
    return allPrimes 
  
def distPrime(arr, allPrimes):
	list1 = list()
	for i in allPrimes: 
		check = True
		for j in arr: 
			if(j % i != 0):
				check = False
		if check:
			list1.append(i)
	return len(list1)

t = int(input())
allPrimes = seive(100000)
for _ in range(t):	
	n = int(input())
	a = [int(x) for x in input().split()][:n]
	q = int(input())
	for i in range(q):
		l, r = input().split()
		l, r = int(l), int(r)
		print(distPrime(a[l-1:r], allPrimes))