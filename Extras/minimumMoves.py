# def calculate(i, s):
#     a = b = 0
#     if i < len(s):
#         t = s[:i] + str(int(not int(s[i]))) + s[i+1:]
#         if i == 0:
#             a = 1 + calculate(i+1, t)
#             b = calculate(i+1, s)
#         else:
#             if s[i] == s[i-1]:
#                 a = 1 + calculate(i+1, t)
#             else:
#                 b = calculate(i+1, s)
#             return max(a, b)

#     return min(a, b)
from itertools import combinations
def minimumMoves(s, d):
    count = 0
    res = [s[x:y] for x, y in combinations(range(len(s) + 1), r = 2) if len(s[x:y]) >= d]
    for i in res:
        if int(i) <= 0:
            count += 1

    return count

# print(minimumMoves("01010101", 2))
# print(minimumMoves("00100", 2))
# print(minimumMoves("010100", 3))
print(minimumMoves("0101010100000111111", 2))
# print(minimumMoves("", 0))