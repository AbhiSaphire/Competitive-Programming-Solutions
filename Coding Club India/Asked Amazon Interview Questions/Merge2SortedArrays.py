def nextGap( gap): 
  
    if (gap <= 1): 
        return 0
    return (gap // 2) + (gap % 2) 
  
def merge(arr1, arr2, n, m): 
  
    gap = n + m 
    gap = nextGap(gap) 
    while gap > 0 :  
      
        # comparing elements in  
        # the first array. 
        i = 0
        while i + gap < n : 
            if (arr1[i] > arr1[i + gap]): 
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i] 
                  
            i += 1
  
        #comparing elements in both arrays. 
        j = gap - n if gap > n else 0
        while i < n and j < m: 
            if (arr1[i] > arr2[j]): 
                arr1[i], arr2[j] = arr2[j], arr1[i] 
                  
            i += 1
            j += 1
  
        if (j < m): 
              
            # comparing elements in the 
            # second array. 
            j = 0
            while j + gap < m : 
                if (arr2[j] > arr2[j + gap]): 
                    arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j] 
                      
                j += 1
                  
        gap = nextGap(gap) 



arr1 = [1,4,6,8,9,10,143,900]
arr2 = [0,3,5,7,9,10,3,678,235345]

merge(arr1, arr2, len(arr1), len(arr2))
print(arr1 + arr2)