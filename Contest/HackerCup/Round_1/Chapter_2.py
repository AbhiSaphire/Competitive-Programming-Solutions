def calc(L, H, W, n):
	P = []
	end = []
	for i in range(n):
		end.append(L[i]+W[i])

	M = 1e9+7
	P.append((W[0] + H[0]) * 2)
	st = 0
	adder = 0
	for i in range(1, n):
		if L[i] > end[i-1]:
			st = i
		if st == i:
			adder = P[-1]
		peri = ((end[i] - min(L[st:i+1]) + max(H[st:i+1])) * 2) + adder
		P.append(peri)

	res = 1
	for i in range(n):
		res = (res * P[i]) %M
	return res %M

def fill(arr, a, b, c, d, k, n):
	for i in range(k, n):
		val = ((a*arr[i-2] + b*arr[i-1] + c) % d) + 1
		arr.append(val)

if __name__ == "__main__":
	t = int(input())
	for i in range(t):
		n, k = input().split()
		n, k = int(n), int(k)
		L = [int(x) for x in input().split()][:k]
		aL, bL, cL, dL = input().split()
		aL, bL, cL, dL = int(aL), int(bL), int(cL), int(dL)
		W = [int(x) for x in input().split()][:k]
		aW, bW, cW, dW = input().split()
		aW, bW, cW, dW = int(aW), int(bW), int(cW), int(dW)
		H = [int(x) for x in input().split()][:k]	
		aH, bH, cH, dH = input().split()
		aH, bH, cH, dH = int(aH), int(bH), int(cH), int(dH)
		if k < n:
			fill(L, aL, bL, cL, dL, k, n)
			fill(W, aW, bW, cW, dW, k, n)
			fill(H, aH, bH, cH, dH, k, n)
		print("Case #{}:".format(i+1), end=" ")
		print(int(calc(L, H, W, n)))