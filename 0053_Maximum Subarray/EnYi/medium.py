class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        while nums[i] <= 0: # find first over zero
            i += 1
            if i == len(nums):
                return max(nums)
        
        max_sum = nums[i]
        sub_sum = max_sum
        
        while i < (len(nums)-1):            
            i += 1
            if sub_sum + nums[i] < 0:
                sub_sum = 0
            else:
                sub_sum += nums[i]
                max_sum = max(max_sum, sub_sum)
        return max_sum