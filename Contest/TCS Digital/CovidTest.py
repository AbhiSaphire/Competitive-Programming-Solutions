def solve(p, d):
	# ?
	
first = input()
n = int(input())
positive = [first]
d = {}
set = ()
for _ in range(n):
	f, s = input().split()
	d[f] = s
	d[s] = f

solve(positive, d)