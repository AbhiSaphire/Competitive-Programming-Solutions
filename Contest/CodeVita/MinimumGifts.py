def findMinGift(emp, n, i, d):
	while i < n:
		if emp[i] > emp[i-1]:
			d[i] = d[i-1] +1
		elif emp[i] == emp[i-1]:
			d[i] = d[i-1]
		elif emp[i] < emp[i-1]:
			if d[i-1] > 1:
				d[i] = 1
			else:
				j = i
				while j-1 >= 0 and emp[j-1] > emp[j]:
					d[j-1] += 1
					j -= 1
				d[i] = 1
		i += 1
	# print(d)
	return sum(d)

if __name__ == "__main__":
	T = int(input())
	for i in range(T):
	    n=int(input())
	    emp=list(map(int,input().split()))
	    temp = [1 for i in range(n)]
	    temp[0] = 1
	    # print(temp)
	    print(findMinGift(emp, n, 1, temp), end='')