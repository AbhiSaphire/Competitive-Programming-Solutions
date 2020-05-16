class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if needle in haystack:
            i = 0
            n = len(needle)
            while i<len(haystack)-n+1:
                if haystack[i:i+n]==needle:
                    return i
                i=i+1
        return -1
