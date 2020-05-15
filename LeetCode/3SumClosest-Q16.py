class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = float('inf')
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                interimSum  = nums[left] + nums[right] + nums[i] - target
                if abs(interimSum) < abs(closestSum):
                    closestSum = interimSum
                if interimSum == 0:
                    return target
                elif interimSum > 0:
                    right -= 1
                else:
                    left += 1
        return closestSum + target
