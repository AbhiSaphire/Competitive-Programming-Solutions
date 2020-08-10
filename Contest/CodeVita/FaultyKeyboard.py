# Python3 Faulty Keyboard

def countDifference(str, S):
	if S not in str:
		return 0
	if S in str:
		return 1
	

def FaultyKeyboard(T, S):
	sum = 0
	for i in T:
		sum += countDifference(i, S)
	return sum

if __name__ == "__main__":
	T = list(input().split())
	S = input()
	print(FaultyKeyboard(T, S))