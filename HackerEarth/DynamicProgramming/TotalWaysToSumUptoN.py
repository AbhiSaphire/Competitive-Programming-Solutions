# Python3 Total Ways to arrange coins {1, 3, 5} to Sum Upto N

# Using Recursion
def Arrangement(N):
	if N < 0:
		return 0
	if N == 0:
		return 1

	return Arrangement(N-1) + Arrangement(N-3) + Arrangement(N-5)

# Using DP
dp = [None for _ in range(10001)]
def Arrangement_DP(n):
	if n < 0:
		return 0
	if n == 0:
		return 1
	if dp[n]:
		return dp[n]
	dp[n] = Arrangement_DP(n-1) + Arrangement_DP(n-3) + Arrangement_DP(n-5)
	return dp[n]

print(Arrangement(10))
print(Arrangement_DP(500))