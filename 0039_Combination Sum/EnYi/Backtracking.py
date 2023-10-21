class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combination = [] # 裝所有組合
        
        def bt(i, path, sum):
            if sum >= target:
                if sum == target: 
                    combination.append(path[:])
                return
            # 找所有 candidates
            for j in range(i, len(candidates)):
                path.append(candidates[j])
                bt(j, path, sum + candidates[j])
                path.pop()

        bt(0, [], 0)

        return combination