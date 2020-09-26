# 0-1 KnapSack Problem using DP

def Knapsack(W, wt, val, n):
	K = [[0 for _ in range(W+1)] for _ in range(n+1)]
	for i in range(1, n+1):
		for w in range(1, W+1):
			if wt[i-1] <= w:
				K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
			else:
				K[i][w] = K[i-1][w]
	return K[n][W]


print(Knapsack(456, [10, 20, 30, 50, 100, 150, 200, 300, 455, 456, 456], [60, 100, 120, 32, 434, 43, 657, 213, 43, 65, 75432], 11))