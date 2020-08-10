def RailwayStation(arrival, departure, n): 
    arrival.sort() 
    departure.sort()
    platform = 1
    result = 1
    j = 0
    i = 1
    while i < n and j < n:
        if arrival[i] <= departure[j]: 
            platform += 1
            i += 1
        elif arrival[i] > departure[j]: 
            platform -= 1
            j+= 1
        result = max(result, platform)
          
    return result

if __name__ == "__main__":
	n = int(input())
	arrival = []
	departure = []
	for i in range(n):
		a, s = input().split()
		arrival.append(int(a))
		departure.append(int(a) + int(s))

	print(RailwayStation(arrival, departure, n))