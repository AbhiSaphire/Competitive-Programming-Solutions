def isAnagram(a,b):
    if len(a) != len(b):
        return False
        
    if a == b:
        return True
        
    for i in range(1, len(a)):
        temp = a[i:] + a[:i]
        if temp == b:
            return True
            
    return False

print(isAnagram("bd", "bd"))