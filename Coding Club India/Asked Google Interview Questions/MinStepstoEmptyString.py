'''
# Given a string s consisting only of letters ’a’ and ’b’. 
# In a single step you can remove one palindromic subsequence from s.
# Return the minimum number of steps to make the given string empty.

'''

def isPalindrome(s):
	i, j = 0, len(s)-1
	while i <= j:
		if s[i] != s[j]:
			return False
		i += 1
		j -= 1
	return True

def MinSteps(s):
	if len(s) == 0:
		return 0
	if s.count('a') == 0 or s.count('b') == 0:
		return 1
	if isPalindrome(s):
		return 1
	return 2

print(MinSteps(""))
# s = "", Steps --> 0

print(MinSteps("aabaabaa"))
# s = "aabaabaa", Steps --> 1

print(MinSteps("ababa"))
# s = "ababa", Steps --> 1

print(MinSteps("abababbabbababaaa"))
# s = "abababbabbababaaa", Steps --> 2