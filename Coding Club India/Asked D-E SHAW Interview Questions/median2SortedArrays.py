def findMedianSortedArrays(arr1, n, arr2, n2):
    '''
    arr1: shorter array
    n1:   len of arr
    arr2: larger array
    n2:   len of array
    return: median
    '''
    #code here
    if n > n2:
        return findMedianSortedArrays(arr2, n2, arr1, n)
    
    min_index = 0
    max_index = n
    while min_index <= max_index:
        i = (min_index + max_index) // 2
        j = (n + n2 + 1) // 2 - i
        
        maxleftX = -999999999 if i == 0 else arr1[i-1]
        minrightX = 999999999 if i == n else arr1[i]
        
        maxleftY = -999999999 if j == 0 else arr2[j-1]
        minrightY = 999999999 if j == n2 else arr2[j]
        
        
        if maxleftX <= minrightY and maxleftY <= minrightX:
            if (n+n2)%2 == 0:
                return (max(maxleftX, maxleftY) + min(minrightX, minrightY))//2
            else:
                return max(maxleftX, maxleftY)
        elif maxleftX > minrightY:
            max_index = i-1
        else:
            min_index = i+1


print(findMedianSortedArrays([1, 3, 8, 9, 15], 5, [7, 11, 18, 19, 21, 25], 6))