def rotateby90(a, n):
    for i in range(n//2):
        for j in range(i, n-i-1):
            a[i][j], a[j][n-i-1], a[n-i-1][n-j-1], a[n-j-1][i] = a[j][n-i-1], a[n-i-1][n-j-1], a[n-j-1][i], a[i][j]
    
    return a

print(rotateby90([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3))


# 1 2 3 			3 6 9
# 4 5 6   ---->		2 5 8
# 7 8 9 			1 4 7