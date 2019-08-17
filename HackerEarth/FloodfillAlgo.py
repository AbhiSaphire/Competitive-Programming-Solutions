def floodFill(mat, j, k, x, y, rows, cols):

    def floodFillHelper(r, c):
        mat[r*cols + c] = k
        if(r > 0 and mat[(r-1)*cols + c] == j):
            floodFillHelper(r-1, c)
        if(c < cols-1 and mat[r*cols + c + 1] == j):
            floodFillHelper(r, c+1)
        if(r < rows-1 and mat[(r+1)*cols + c] == j):
            floodFillHelper(r+1, c)
        if(c > 0 and mat[r*cols + c - 1] == j):
            floodFillHelper(r, c-1)
    
    floodFillHelper(x, y)
    print(' '.join(map(str, mat)))

t = int(input())
for _ in range(t):
    rows, cols = map(int, input().split())
    mat = list(map(int, input().split()))
    x, y, k = map(int, input().split())
    j = mat[x*cols + y]
    floodFill(mat, j, k, x, y, rows, cols)
