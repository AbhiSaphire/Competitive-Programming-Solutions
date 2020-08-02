def powerof4(n):
	if not n&3:
		return "True"
	return "False"

if __name__ == "__main__":
	t = int(input())
	for i in range(t):
		n = int(input())
		print(powerof4(n))