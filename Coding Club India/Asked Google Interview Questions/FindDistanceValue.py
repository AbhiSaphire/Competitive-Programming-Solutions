import bisect
def findTheDistanceValue(arr1, arr2, d) -> int:
    arr2.sort()
    rv = 0
    for val in arr1:
        index = bisect.bisect(arr2, val)
        for dx in (-1, 0, 1):
            x = dx + index
            if 0 <= x < len(arr2) and abs(arr2[x] - val) <= d: break
        else:
            rv += 1
    return rv


print(findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2))