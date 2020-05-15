class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()  # use set
        nums.sort()
        if (not nums) or nums[0] > 0 or nums[len(nums)-1] < 0:
            return []
        for k in range(len(nums)-2):
            if nums[k] > 0:
                break
            # not check duplicate value
            target = 0-nums[k]
            i = k+1
            j = len(nums)-1
            while(i < j):
                if nums[i]+nums[j] == target:
                    tmp = (nums[k], nums[i], nums[j])
                    res.add(tmp)  # add tuple to set
                    while(i < j and nums[i] == nums[i+1]):
                        i = i+1
                    while(i < j and nums[j] == nums[j-1]):
                        j = j-1
                    i = i+1
                    j = j-1
                elif nums[i]+nums[j] < target:
                    i = i+1
                else:
                    j = j-1
        return [list(r) for r in res]
        
