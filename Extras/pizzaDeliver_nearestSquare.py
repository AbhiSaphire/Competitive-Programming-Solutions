from math import sqrt
def nearest_square(n):
    return round(sqrt(n))**2

def pizza(n):
    count=0
    i=1
    while(n!=0 and n!=1):
        near = nearest_square(n)
        if near == n:
            count+=1
            break
        if near > n:
            n = near - n
        elif near < n:
            n = n - near
        count += 1
        i+=1
    if n==1:
        print(count+1)
    else:
        print(count)

T=int(input())
for i in range(T):
    n=int(input())
    pizza(n)