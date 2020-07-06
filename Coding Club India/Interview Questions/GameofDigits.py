def smallestK(n):
    if n >=0 and n < 10:
        return n
    l = []
    for i in range(9, 1, -1):
        while n%i == 0:
            l.append(i)
            n //= i
            
    if n != 1:
        return -1
    
    returner = 0
    while len(l):
        returner = returner * 10 + l[-1]
        l.pop()
    
    return returner

print(smallestK(140))