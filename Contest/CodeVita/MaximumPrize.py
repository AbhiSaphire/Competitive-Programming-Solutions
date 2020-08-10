def maximum_prize(l,n):
    p = 0
    length = 0
    for i in l:
        if i != 0:
            break
        else:
            length += 1
    if length == len(l):
        return 0
    if len(l) == 3:
        if l[0] < l[1] and l[2] < l[1]:
            p += (l[0] * l[1]) + (l[1] * l[2]) + l[1]
            return(p)
    while (len(l) > 2):
        l1 = []
        for i in range(len(l)):
            if i == 0:
                l1.append(l[i] * l[i+1])
            elif i == len(l) -1:
                l1.append(l[i] * l[i-1])
            else:
                if l[i] != 0:
                    if l[i-1] > l[i+1]:
                        l1.append((l[i] * l[i-1]) + l[i+1])
                    else:
                        l1.append((l[i] * l[i+1]) + l[i-1])
                else:
                    if l[i-1] > l[i+1]:
                        l1.append((l[i] * l[i+1]) + l[i-1])
                    else:
                        l1.append((l[i] * l[i-1]) + l[i+1])
        max1 = 0
        x = 0
        for i in range(0, len(l1)):
            if(l1[i] > max1):
                max1 = l1[i]
                k = i
        x = l[k]
  
        if(l1.count(max1) > 1):
            y = k+1
            for j in range(y, len(l1)):
                if(l1[j] == max1):
                    if(x > l[j]):
                        x = l[j]
                        k = j
        p = p + max1
        del l[k:k+1]
        if len(l)==3:
            if l[0] < l[1] and l[2] < l[1]:
                p += (l[0] * l[1]) + (l[1] * l[2]) + l[1]
                return(p)
    i = 0
    if len(l) == 2:
        if(l[i] > l[i+1]):
            p = p + l[i] * l[i+1] + l[i]
        else:
            p = p + l[i] * l[i+1] + l[i+1]
        return(p)
    else:
        return(l[0])
    
if __name__ == "__main__":
    n=int(input())
    l=list(map(int,input().split()))
    print(maximum_prize(l,n), end='')