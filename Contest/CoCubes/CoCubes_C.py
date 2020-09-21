def countPairsWithDiffK(arr,n,k): 
    count = l = r = 0
    arr.sort()
    while r < n: 
        if arr[r] - arr[l] == k: 
            count += 1
            l += 1
            r += 1
 
        elif arr[r] - arr[l] > k:
            l += 1
        else: 
            r += 1
    return count 

if __name__ == '__main__': 
    arr = [int(x) for x in input().split()]
    n = len(arr)
    k = int(input())
    print(countPairsWithDiffK(arr, n, k))