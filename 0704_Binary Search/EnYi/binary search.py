class Solution:    
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if nums[left] > target or nums[right] < target:
            return -1
        while left != right:
            a = floor((left + right)/2)
            if target == nums[a]:
                return a
            elif left == a:
                if nums[a+1] == target:   
                    return a+1
                else:
                    return -1
            elif target > nums[a]:
                left = a
            elif target < nums[a]:
                right = a
        if nums[left] == target:
            return 0
        else:
            return -1