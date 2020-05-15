import re
class Solution:
    def myAtoi(self, str: str) -> int:
        mi = -2**31
        mx = 2**31 - 1
        num = x = 0
        sign = 1
        mod = mx % 10
        #discard all leading whitespaces
        while x < len(str) and str[x] == ' ':
            x += 1
        #check if there's a sign
        if x < len(str):
            if str[x] == '-':
                sign = -1
                x += 1
            elif str[x] == '+':
                x += 1
        while x < len(str):
            if str[x].isdigit():
                #check overflow
                if (num > mx // 10 or (num == mx // 10 and int(str[x]) > mod)):
                    return mx if sign > 0 else  mi
                num *= 10
                num += int(str[x])
                x += 1
            else:
                break
        return num * sign
