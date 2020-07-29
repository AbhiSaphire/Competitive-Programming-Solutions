def Maximum_Sum(mat,n,k):
    if k > n:
        return 0
    stripSum = [[0 for i in range(n)] for j in range(n-k+1)]
    
    for j in range(n):
        sum = 0
        for i in range(k):
            sum += mat[i][j]
        stripSum[0][j] = sum
        
        for i in range(1, n-k+1):
            sum += (mat[i+k-1][j] - mat[i-1][j])
            stripSum[i][j] = sum
        
    print(stripSum)
    max_sum = -999999999
    for i in range(n-k+1):
        sum = 0
        for j in range(k):
            sum += stripSum[i][j]
        if sum > max_sum:
            max_sum  = sum

        for j in range(1, n-k+1):
            sum += (stripSum[i][j+k-1] - stripSum[i][j-1])
            if sum > max_sum:
                max_sum = sum
                
    return max_sum

print(Maximum_Sum([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 2, 1]], 5, 3))