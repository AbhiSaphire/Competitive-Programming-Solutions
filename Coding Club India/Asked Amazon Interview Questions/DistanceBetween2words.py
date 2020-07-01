import math
def distance(s, w1, w2): 
	words = s.split(" ") 
	n = len(words)  
	min_dist = math.inf
	for i in range(n): 
		if words[i] == w1 or words[i] == w2: 
			prev = i 
			break
	while i < n: 
		if words[i] == w1 or words[i] == w2: 
			if words[prev] != words[i] and (i - prev) < min_dist : 
				min_dist = i - prev - 1
				prev = i 
			else: 
				prev = i 
		i += 1		
	return min_dist 

s = "hello hello abhi hello kaun ab ye kya kaun"
w1 = "abhi"
w2 = "kaun"
print(distance(s, w1, w2)) 
