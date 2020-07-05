# Python3 program to find Intersection of two
# Sorted Arrays (Handling Duplicates)
def IntersectionArray(a, b, n, m):
    '''
    :param a: given sorted array a
    :param n: size of sorted array a
    :param b: given sorted array b
    :param m: size of sorted array b
    :return: array of intersection of two array or -1
    '''

    Intersection = []
    i = j = 0
    
    while i < n and j < m:
        if a[i] == b[j]:

            # If duplicate already present in Intersection list
            if len(Intersection) > 0 and Intersection[-1] == a[i]:
                i+=1
                j+=1

            # If no duplicate is present in Intersection list
            else:
                Intersection.append(a[i])
                i+=1
                j+=1
        elif a[i] < b[j]:
            i+=1
        else:
            j+=1
            
    if not len(Intersection):
        return [-1]
    return Intersection

# Driver Code
if __name__ == "__main__":

    arr1 = [1, 2, 2, 3, 4]
    arr2 = [2, 2, 4, 6, 7, 8]

    l = IntersectionArray(arr1, arr2, len(arr1), len(arr2))
    print(*l)

#  This code is submited by AbhiSaphire