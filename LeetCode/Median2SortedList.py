class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 or not nums2:
            if not nums1:
                if len(nums2)%2==0:
                    return (nums2[len(nums2)//2-1]+nums2[len(nums2)//2])/2
                else:
                    return nums2[(len(nums2)-1)//2]
            else:
                if len(nums1)%2==0:
                    return (nums1[len(nums1)//2-1]+nums1[len(nums1)//2])/2
                else:
                    return nums1[(len(nums1)-1)//2]
        elif len(nums1)==1 or len(nums2)==1:
            if len(nums1)<=len(nums2):
                return self.find_median_single(nums1,nums2)
            else:
                return self.find_median_single(nums2,nums1)
        else:
            # both nums1 and num2 greater than 1
            m=len(nums1)
            n=len(nums2)
            if m>=n:
                if (m+n)%2==1:
                    # need to return 1
                    return self.find_median(nums1,nums2, 0, 2*(n-1), (m+n+1)//2)
                else:
                    return (self.find_median(nums1,nums2, 0, 2*(n-1), (m+n)//2)+self.find_median(nums1,nums2, 0, 2*(n-1), (m+n)//2+1))/2
            else:
                if (m+n)%2==1:
                    # need to return 1 number
                    return self.find_median(nums2,nums1, 0, 2*(m-1), (m+n+1)//2)
                else:
                    return (self.find_median(nums2,nums1, 0, 2*(m-1), (m+n)//2)+self.find_median(nums2,nums1, 0, 2*(m-1), (m+n)//2+1))/2
        
    def find_median_single(self, nums1, nums2):
        # len(nums1)<=len(nums2)
        if len(nums1)==1 and len(nums2)==1:
            return (nums1[0]+nums2[0])/2
        else:
            if (len(nums1)+len(nums2))%2==1:
                # single number
                if nums1[0]>nums2[len(nums2)//2]:
                    return nums2[len(nums2)//2]
                else:
                    return max(nums1[0],nums2[len(nums2)//2-1])
            else:
                # return double number
                if nums1[0]>nums2[(len(nums2)+1)//2]:
                    return (nums2[(len(nums2)-1)//2]+nums2[(len(nums2)+1)//2])/2
                else:
                    return (nums2[(len(nums2)-1)//2]+max(nums1[0],nums2[(len(nums2)-3)//2]))/2
        
    def find_median(self, A, B, low, high, target):
        # B is shorter one len(B)<=len(A) and len(B)> 1
        j=(low+high)//2
        i=target-2-j
        # cases when the median 
        if j<0:
            # if j smaller than zero
            # that means the median comes from array A
            return A[target-1]
        elif j==0:
            # see if it satisfy the condition
            if i==len(A)-1:
                if A[i]<=B[j+1]:
                    return max(A[i],B[j])
                else:
                    # move to the right
                    return self.find_median(A,B,j+1,high, target)
            else:
                # see if condition is satisfied
                if max(A[i],B[j])<=min(A[i+1],B[j+1]):
                    return max(A[i],B[j])
                else:
                    # move to the right
                    if A[i]>B[j+1]:
                        return self.find_median(A,B, j+1, high, target)
                    elif B[j]>A[i+1]: 
                        # move to the left
                        return self.find_median(A,B, low, j-1, target)
        elif j==len(B)-1:
            # see if i<=0:
            if i<0:
                # compare B[j] with A[2]
                i=0
                if B[j]<=A[i+1]:
                    if A[i]>=B[j]:
                        return B[j]
                    else:
                        return max(A[i],B[j-1])
                else:
                    # move to the left
                    return self.find_median(A,B,low, j-1,target)
            else:
                # initially if it satisfy the condition
                if B[j]<=A[i+1]:
                    return max(A[i],B[j])
                else:
                    # move to the left
                    return self.find_median(A,B,low, j-1,target)
        else:
            if max(A[i],B[j])<=min(A[i+1], B[j+1]):
                return max(A[i],B[j])
            else:
                if B[j]>A[i+1]:
                    # move to the left
                    return self.find_median(A,B,low, j-1,target)
                    # move to the right
                elif B[j+1]<A[i]:
                    if j+1>high:
                        return B[j+1]
                    else:
                        return self.find_median(A,B,j+1,high, target)
