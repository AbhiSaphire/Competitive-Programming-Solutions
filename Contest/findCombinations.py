def findCombinationsUtil(arr, index, num, reducedNum, max_sum, prices, l): 
	if (reducedNum < 0):
		return; 
	if (reducedNum == 0):
		suma = 0
		for i in range(index): 
			suma += prices[arr[i]-1] 
		max_sum = max(suma, max_sum)
		l.append(max_sum)
		return
		
	prev = 1 if(index == 0) else arr[index - 1]
	for k in range(prev, num + 1):
		arr[index] = k
		findCombinationsUtil(arr, index + 1, num, reducedNum - k, max_sum, prices, l)

def findCombinations(n, prices): 
	arr = [0] * n;
	l = []
	findCombinationsUtil(arr, 0, n, n, 0, prices, l);
	print(max(l))

if __name__ == '__main__':
	t = int(input())
	while(t):
		n = int(input())
		prices = [int(x) for x in input().split()][:n]
		findCombinations(n, prices);
		t -= 1
