if __name__ == "__main__":
	def isVowel(c):
		return c=='a' or c=='e' or c=='i' or c=='o' or c=='u'
	def isCons(c):
		return not isVowel(c)

	firstV = False
	def findsub(string):
		global maxSub
		global maxSublength
		for i in range(len(string)):
			if isVowel(string[i]):
				for j in range(len(string)-1, i-1, -1):
					if isCons(string[j]):
						subString = string[i:j]
						tempMaxSublength = [ord(num) for num in subString]
						if sum(tempMaxSublength) > maxSublength:
							maxSub, maxSublength = subString, sum(tempMaxSublength)
						for k in range(1, len(subString)):
							findsub(subString[k:])
	
	maxSublength = 0
	maxSub = ""
	string = input()
	findsub(string)
	print(maxSub)


