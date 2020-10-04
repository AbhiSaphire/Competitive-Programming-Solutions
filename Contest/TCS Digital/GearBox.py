r1, r2, r3 = input().split()
r1, r2, r3 = int(r1), int(r2), int(r3)
rot = int(input())

result = (rot // (r3 // r1))
print(result, end='')