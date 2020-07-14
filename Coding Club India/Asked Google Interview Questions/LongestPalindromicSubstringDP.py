def longestPalindrome(s):
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = True
        
    max_length = 1
    first = 99999999999
    start = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start = i
            max_length = 2
            first = min(first, start)
    
    for k in range(3, n+1):
        for i in range(n-k+1):
            j = i + k -1
            if dp[i+1][j-1] and s[i] == s[j]:
                dp[i][j] = True
                if k > max_length:
                    print(k, " ", max_length)
                    start = i
                    max_length = k

    if max_length == 2:
        return s[first:first+max_length]
    # print(start, max_length)
    else:
        return s[start:start+max_length]


print(longestPalindrome("aaaabbaa"))
print(longestPalindrome("kjqlrzzfmlvyoshiktodnsjjp"))