from itertools import permutations
def isPalindrome(s):
    i, j = 0, len(s)-1
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
        
s = input()
l = []
for i in permutations(s):
    temp = ""
    for j in i:
        temp += j
    print(temp)
    if isPalindrome(temp):
        l.append(temp)
    l.sort()
    print(l[-1])