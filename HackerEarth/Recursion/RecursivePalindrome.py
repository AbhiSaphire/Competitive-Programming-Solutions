def RecursivePalindrome(s):
	if len(s) <= 1:
		return True
	if s[0] != s[-1]:
		return False
	if s[0] == s[-1]:
		return RecursivePalindrome(s[1:-1])

print(RecursivePalindrome("abba"))		# True
print(RecursivePalindrome("abvba"))		# True
print(RecursivePalindrome("abdc"))		# False
print(RecursivePalindrome("aabba"))		# False