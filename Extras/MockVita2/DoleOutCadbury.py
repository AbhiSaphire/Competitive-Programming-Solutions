min_length = int(input())
max_length = int(input())
min_width = int(input())
max_width = int(input())

dp = [[0 for i in range(max_width+1)] for i in range(max_length+1)]
for i in range(len(dp)):
	dp[i][1] = i
for i in range(len(dp[0])):
	dp[1][i] = i
	
def findsquares(n, m):
	if dp[n][m]:
		return dp[n][m]
	if n == 0 or m == 0:
		return 0
	if (n == 1 and m == 1) or n == m:
		return 1
	if (n == 1 and m == 2) or (n == 2 and m == 1):
		return 2
	if n > m:
		dp[n][m] += findsquares(n-m, m)+1
	elif n < m:
		dp[n][m] += findsquares(n, m-n)+1
	if m <= max_length and n <= max_width:
		dp[m][n] = dp[n][m]
	return dp[n][m]

result = 0
for i in range(min_length, max_length+1):
	j = min_width
	while j <= max_width:
		result += findsquares(i, j)
		# print(result, " ", i, " ", j)
		j +=1
print(result, end = '')
# print(dp)