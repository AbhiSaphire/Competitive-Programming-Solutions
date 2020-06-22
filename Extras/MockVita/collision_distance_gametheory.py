import math

def calculate_collision(l):
	count = 0
	distance = []
	for i in range(len(l)):
		dist = math.sqrt(l[i][0]**2 + l[i][1]**2)
		distance.append(dist/l[i][2])
	
	for i in range(len(distance)):
		val = distance[i+1:].count(distance[i])
		if val >= 1:
			count += val
	return count

c = int(input())
l = []
while c:
	x, y, v = input().split()
	l.append([int(x), int(y), int(v)])
	c -= 1
print(calculate_collision(l))