MAX = 100000
prime = [True for i in range(MAX + 1)]
append_prime = []
def Sieve(): 
    prime[1] = False
    for p in range(2, MAX+1):  
        if (prime[p] == True):
            i = p * 2
            while(i <= MAX): 
                prime[i] = False
                i = i + p
    prev = 0
    for i in range(MAX+1):
        if prime[i]:
            append_prime.append(i+prev)
            prev = append_prime[-1]

q= int(input())
Sieve()
for i in range(q):
    n = int(input())
    print(append_prime[n])