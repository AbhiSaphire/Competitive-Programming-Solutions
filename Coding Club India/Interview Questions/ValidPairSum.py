from bisect import bisect_left
def findNumOfPair(array, n): 
    array.sort()
    count = 0
    for i in range(n):
        if array[i] <= 0:
            continue
        j = bisect_left(array, -array[i]+1)
        count += i - j
    
    return count

print(findNumOfPair([3, -2, 1], 3))