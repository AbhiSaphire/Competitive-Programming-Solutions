def solution(l, n):
	localSum = 0
	maxSum = float('-inf')
	i = 0
	j = n-1-i
	while i<j:
		localSum ^= l[i]^l[j]
		if localSum > maxSum:
			maxSum = localSum
		else:
			summation = localSum
			summation ^= l[i-1]^l[j+1]
			if summation >= maxSum:
				maxSum = summation
		i += 1
		j -= 1
	return maxSum

if __name__ == '__main__':
	n = int(input())
	l = [int(x) for x in input().split()][:n]
	print(solution(l, n))