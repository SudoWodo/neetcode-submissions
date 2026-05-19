class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        result_set = set()
        def dfs(start,curr_sum, subset):

            if curr_sum > target:
                return
            elif curr_sum == target:
                result.append(subset.copy())
                result_set.add(frozenset(subset.copy()))
                return
            
            for idx in range(start, len(nums)):
                subset = subset + [nums[idx]]
                dfs(idx, nums[idx] + curr_sum, subset)
                subset.pop()
        
        dfs(0, 0, [])
    

        return result