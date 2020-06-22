def sort_list(list1):
	list1.sort(key=lambda x: (x[2], x[0]), reverse=False)
	for x in list1:
		temp = list(list1.pop(0))
		temp[0], temp[1], temp[2] = temp[1], temp[2], temp[0]
		list1.append(tuple(temp))

def find4Sum(nums):
	res = set()
	nums.sort()
	if (not nums) or nums[0] > 0 or nums[len(nums)-1] < 0:
		return []
	for l in range(len(nums)-3):
		for k in range(l+1, len(nums)-2):
			target = 2-nums[k]-nums[l]
			i = k+1
			j = len(nums)-1
			while(i < j):
				if nums[i]+nums[j] == target:
					tmp = (nums[k], nums[i], nums[j], nums[l])
					res.add(tmp)
					while(i < j and nums[i] == nums[i+1]):
						i = i+1
					while(i < j and nums[j] == nums[j-1]):
						j = j-1
					i = i+1
					j = j-1
				elif nums[i]+nums[j] < target:
					i = i+1
				else:
					j = j-1
	return [list(r) for r in res]

if __name__ == '__main__':

	#____________________First Question_________________________
	list1 = [("Harry Potter", 1999, 1000), ("Gone Girl", 1960, 500), ("Abhishek Blog", 1960, 500), ("Girl on the Train", 2012, 1200), ("Happy Bot", 2020, 100), ("Harry Potter 2", 1890, 1899)]
	sort_list(list1)
	print(list1)

	#_____________________Second Question_________________________
	nums = [int(x) for x in input().split()]
	print(find4Sum(nums))
