def getPairsCount(arr, n, sum):      
    count, s = 0, {}
    for i in range(0, n): 
        temp = sum-arr[i] 
        if (temp in s): 
            count += s[temp]
        if arr[i] not in s:
        	s[arr[i]] = 1
        else:
        	s[arr[i]] += 1
    return count

print(getPairsCount([1, 1, 1, 1, 1], 5, 2))