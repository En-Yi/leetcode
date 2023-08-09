class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # define hashmap
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        # find complement. if the corresponding item is not equal to i, then return the pair    
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]] 