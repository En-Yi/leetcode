class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower, upper = 0, len(nums) - 1

        if len(nums) == 1:
            return -1*(nums[0] != target)
        
        while upper - lower > 1:
            
            if nums[(lower + upper) // 2] == target:
                return (lower + upper) // 2
            
            # 這個 while 目的在於限縮 target 可能的範圍
            # 2 cases:
            # 1. lower < upper (範圍已排序)
            if nums[lower] <= nums[upper]:
                if nums[lower] <= target <= nums[(lower + upper) // 2]:
                    upper = (lower + upper) // 2
                elif nums[(lower + upper) // 2] <= target <= nums[upper]:
                    lower = (lower + upper) // 2
                else:
                    return -1

            # 2. lower > upper
            else:
                if nums[lower] <= target <= nums[(lower + upper) // 2]:
                    upper = (lower + upper) // 2                    
                elif nums[(lower + upper) // 2] <= target <= nums[upper]:
                    lower = (lower + upper) // 2
                elif nums[lower] > nums[(lower + upper) // 2]:                    
                    if target >= nums[lower] or target <= nums[(lower + upper) // 2]:
                        upper = (lower + upper) // 2                        
                    else:
                        return -1
                elif nums[upper] < nums[(lower + upper) // 2]:
                    if target >= nums[(lower + upper) // 2] or target <= nums[upper]:
                        lower = (lower + upper) // 2
                    else:
                        return -1
        if nums[lower] == target:
            return lower
        elif nums[upper] == target:
            return upper
        else:
            return -1