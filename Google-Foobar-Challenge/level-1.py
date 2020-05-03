# Return a list fo squares that can be made from a large square area.
# If area = 12 return [9, 1, 1, 1] i.e, four squares (3x3), (1x1), (1x1), (1x1)

def solution(area):
	returner = []
	while(area):
		sample = area ** 0.5
		returner.append(int(sample) ** 2)
		area = area - (int(sample) ** 2)
	return (returner)
