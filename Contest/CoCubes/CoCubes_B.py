MAX_CHARS = 26

def isValid(count, k):  
    val = 0
    for i in range(MAX_CHARS):  
        if count[i] > 0:  
            val += 1 
    return (k >= val)  

def kUniques(s): 
    k, u, n = 2, 0, len(s) 
    count = [0] * MAX_CHARS 
    for i in range(n):  
        if count[ord(s[i])-ord('a')] == 0:  
            u += 1
        count[ord(s[i])-ord('a')] += 1

    curr_start = curr_end = max_window_start = 0
    max_window_size = 1
    count = [0] * len(count)
    count[ord(s[0])-ord('a')] += 1

    for i in range(1,n): 
        count[ord(s[i])-ord('a')] += 1
        curr_end+=1 
        while not isValid(count, k):  
            count[ord(s[curr_start])-ord('a')] -= 1
            curr_start += 1

        if curr_end-curr_start+1 >= max_window_size:  
            max_window_size = curr_end-curr_start+1
            max_window_start = curr_start  
    print (s[max_window_start : max_window_start + max_window_size]) 
   
s = input()
kUniques(s)