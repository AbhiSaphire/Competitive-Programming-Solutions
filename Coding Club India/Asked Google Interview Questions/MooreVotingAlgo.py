def findCandidate(A): 
    maj_index = 0
    count = 1
    for i in range(len(A)): 
        if A[maj_index] == A[i]: count += 1
        else: count -= 1
        if count == 0: maj_index, count = i, 1
    return A[maj_index] 
   
def isMajority(A, cand, k): 
    count = 0
    for i in range(len(A)): 
        if A[i] == cand: count += 1
    if count > len(A)/k: return True
    else: return False

def printMajority(A, k): 
    cand = findCandidate(A) 
    if isMajority(A, cand, k) == True: 
        print(cand) 
    else: 
        print("No Majority Element") 

printMajority([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,4, 4, 5, 6, 7, 8, 4, 4, 5, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 4], 3)