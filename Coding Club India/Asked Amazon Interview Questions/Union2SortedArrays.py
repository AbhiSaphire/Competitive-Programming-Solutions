def Union2SortedArrays(arr1, arr2):
	m = arr1[-1]
	n = arr2[-1]
	ans = 0
          
	if m > n:  
		ans = m  
	else: 
		ans = n  

	returner = []
	newtable = [0] * (ans + 1)
	returner.append(arr1[0]) 
	newtable[arr1[0]] += 1
	for i in range(1, len(arr1)):  
		if arr1[i] != arr1[i - 1]:  
			returner.append(arr1[i])
			newtable[arr1[i]] += 1
            
	for j in range(0, len(arr2)):  
		if newtable[arr2[j]] == 0:
			returner.append(arr2[j])  
			newtable[arr2[j]] += 1

	return returner


print(Union2SortedArrays([1, 2, 3, 4, 5], [1, 2, 3]))