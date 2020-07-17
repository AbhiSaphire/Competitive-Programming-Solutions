from math import floor, log10

n = int(input())
l = [int(x) for x in input().split()][:n]

def calc(n):
	large = 0
	small = 9
	while n:
		r = n%10
		large = max(large, r)
		small = min(small, r)
		n //= 10
	return large, small

for i in range(n):
	large, small = calc(l[i])
	val = (large*11 + small*7)%100
	l[i] = floor(val / (10**floor(log10(val))))

print(l)
# l = [1, 1, 4, 7, 4, 1, 1, 1]
pairs = 0
even = {}
odd = {}
for i in range(n):
	if i&1:
		if l[i] not in odd:
			odd[l[i]] = 1
		else:
			odd[l[i]] += 1
	else:
		if l[i] not in even:
			even[l[i]] = 1
		else:
			even[l[i]] += 1
# print(even)	
# print(odd)
result = set()
for k, v in even.items():
	if (k, 2) not in result:
		if v == 2:
			pairs += 1
			result.add((k, 1))
		elif v > 2:
			pairs += 2
			result.add((k, 2))
for k, v in odd.items():
	if (k, 2) not in result:
		if v == 2:
			pairs += 1
			result.add((k, 1))
		elif v > 2 and (k, 1) in result:
			pairs += 1
			result.add((k, 2))
		elif v > 2 and (k, 1) not in result:
			pairs += 2
			result.add((k, 2))
# print(result)
print(pairs, end='')