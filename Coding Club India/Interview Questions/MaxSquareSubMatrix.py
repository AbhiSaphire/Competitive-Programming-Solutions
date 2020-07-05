def solution(M):
    R = len(M) # no. of rows in M[][] 
    C = len(M[0]) # no. of columns in M[][] 
  
    S = [[0 for k in range(C)] for l in range(R)]  
    for i in range(1, R): 
        for j in range(1, C): 
            if (M[i][j] == 1): 
                S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
            else: 
                S[i][j] = 0

    max_of_s = S[0][0] 
    max_i = 0
    max_j = 0
    for i in range(R): 
        for j in range(C): 
            if (max_of_s < S[i][j]): 
                max_of_s = S[i][j] 
                max_i = i 
                max_j = j 

    return max_of_s*max_of_s

print(solution([[0, 1, 1, 0, 1], 
                [1, 1, 0, 1, 0], 
                [0, 1, 1, 1, 0], 
                [1, 1, 1, 1, 0], 
                [1, 1, 1, 1, 1], 
                [0, 0, 0, 0, 0]]))