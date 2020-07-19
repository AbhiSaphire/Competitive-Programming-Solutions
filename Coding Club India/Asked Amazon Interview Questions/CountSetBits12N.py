# ---------------------------------LogN Solution-------------------------
def logbase2(n):
    m = 0
    while n > 1:
        n >>= 1
        m += 1
    return m
    
def CountBits(n):
    m = logbase2(n)
    if n == 0:
        return 0
    def nextMSB(n, m):
        temp = 1 << m
        while n < temp:
            temp = temp >> 1
            m -= 1
        return m
    
    m = nextMSB(n, m)
    if (n == (1 << (m+1))-1):
        return ((m+1) * (1 << m))
    n = n - (1 << m)
    return (n + 1) + CountBits(n) + m * (1 << (m -1))

# -----------------------------------Mathematically-------------------------

def CountBits_Methematically(n):
    sum=0
    for i in range(32):
        blockSize = 2**(i+1)
        completeBlocks = (n+1)//blockSize
        number_of_ones = 2**i * completeBlocks
        incompleteBlock = (n+1) % blockSize
        remainder_ones = incompleteBlock - 2**i
        if remainder_ones > 0:
            number_of_ones += remainder_ones
        sum += number_of_ones
    return sum

print(CountBits(4))
print(CountBits_Methematically(4))
print(CountBits(15))
print(CountBits_Methematically(15))



# N = 6 
#                   0 | 0 0   -|
#                   0 | 0 1    |
#                   0 | 1 0    | -> b*2^(b-1)
#                   0 | 1 1   -|
#                   - - - -
#               |-  1 | 0 0   -|
# n-(1<<m)+1 -> |   1 | 0 1    | -> by recursion using nextMSB
#               |-  1 | 1 0   -|