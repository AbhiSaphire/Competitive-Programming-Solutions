from itertools import permutations

def find_prime(n1, n2): 
    prime = [True for i in range(n2+1)] 
    p = 2
    while (p * p <= n2): 
        if prime[p]: 
            for i in range(p * p, n2+1, p): 
                prime[i] = False
        p += 1
    returner = []
    for i in range(n1, n2+1):
        if prime[i]:
            returner.append(i)
    return returner


def find_comb(prime_list):
    returner = []
    permutation = [*permutations(prime_list, 2)]
    for i in permutation:
        returner.append(int(str(i[0]) + str(i[1])))
    return returner


def isPrime(n):
    if (n <= 1) or (n % 2 == 0 or n % 3 == 0) : return False
    if (n <= 3) : return True
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : return False
        i += 6
    return True

def find_prime_comb(l):
    returner, prime_set = [], set()
    for i in l:
        if isPrime(i) and i not in prime_set:
            returner.append(i)
            prime_set.add(i)
    return returner


def fibo(a, b, n):
    returner = [0] * n
    returner[0], returner[1] = a, b
    for i in range(2, n):
        returner[i] = returner[i-1] + returner[i-2]
    return returner[-1]

if __name__ == "__main__":
    n1, n2 = input().split()
    prime_comb = find_prime_comb(find_comb(find_prime(int(n1), int(n2))))
    a, b = min(prime_comb), max(prime_comb)
    print(fibo(a, b, len(prime_comb)), end="")