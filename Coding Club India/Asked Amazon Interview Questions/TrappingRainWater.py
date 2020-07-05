def trappingWater(arr,n):
    left = [0] * (n)
    right = [0] * (n)

    maxl = maxr = 0
    for i in range(n):
        left[i] = max(arr[i], maxl)
        if arr[i] > maxl:
            maxl = arr[i]

    for i in range(n-1, -1, -1):
        right[i] = max(arr[i], maxr)
        if arr[i] > maxr:
            maxr = arr[i]

    for i in range(n):
        mini = min(left[i], right[i])
        arr[i] -= mini

    volume = 0
    for i in range(n):
        volume += abs(arr[i])

    return volume

print(trappingWater([1, 1, 5, 2, 7, 6, 1, 4, 2, 3], 10))