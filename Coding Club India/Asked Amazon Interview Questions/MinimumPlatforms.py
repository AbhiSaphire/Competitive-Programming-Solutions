def minPlatform(n, arr, dep):
	arr.sort() 
    dep.sort() 
    plat_needed = 1
    result = 1
    i = 1
    j = 0
    while (i < n and j < n): 
        if (arr[i] <= dep[j]):
            plat_needed+= 1
            i+= 1
        elif (arr[i] > dep[j]):
            plat_needed-= 1
            j+= 1
        if (plat_needed > result):  
            result = plat_needed 
          
    return result

if __name__ == "__main__":
	arr = [0900,  0940, 0950, 1100, 1500, 1800]
	dep = [0910, 1200, 1120, 1130, 1900, 2000]
	print(minPlatform(len(arr), arr, dep))