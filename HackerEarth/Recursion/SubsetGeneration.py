# Subset or Subsequence generation 
# Input - "abc",  Output - "a", "b", "c", "ab", "ac", "abc", "bc"
# Input - "abcd", Output - "a", "b", "c", "d", "ab", "ac", "ad", "abc", "acd", "abd", "abcd", "bc", "bcd", "bd", "cd"

# "abc" "ab" "ac" "a" "bc" "b" "c"  ""
#    \   /	   \  /     \  /     \ /
#     "ab"	    "a"		 "b"	  ""
#   	\       /          \      /
#   	   "a"                ""
#   	     \                /
#   	  		  curr = ""

# Options - 
# 1) Consider curr as a part of subset
# 2) Do not consider curr as a part of subset

def Subset(s, index = 0, curr = ''):
	if index == len(s):
		print(curr, end = ' ')
		return
	Subset(s, index + 1, curr + s[index])
	Subset(s, index + 1, curr)

Subset("abc")
print()
Subset("abcd")
print()